import datetime
from enum import Enum
from typing import Any, Union, List, Tuple, Optional

from pymongo import MongoClient

import rxconfig

ChatState = Enum(
    'ChatState', [
        'INITED',
        'BLOCKED',

        'WaitForNationalId',
        'WaitForOTP',
        'WaitForCaptcha',
        'LoggedIn',
        'HasAccess',
        'HasManualAccess',
    ]
)


class Mongo:
    def __init__(self, mongo_db) -> None:
        self.mongo_db = mongo_db
        self.client = MongoClient(**rxconfig.MONGO_CONFIG)
        self.db = self.client[self.mongo_db]

    def drop_database(self):
        self.client.drop_database(self.mongo_db)

    def store_event(self, event: dict) -> None:
        # pprint(event)
        self.db.events.insert_one(event)

    def store_check_level(self, check_level: dict) -> None:
        # pprint(check_level)
        self.db.check_level.insert_one(check_level)

    def delete_user(self, user_id: int):
        self.db.users.delete_one({'user_id': user_id})

    def get_user(self, key, value) -> Union[None, dict]:
        return self.db.users.find_one({key: value})

    def get_user_by_id(self, user_id: int) -> Union[None, dict]:
        return self.get_user('user_id', user_id)

    def get_chat_state(self, user_id: int) -> Union[ChatState, None]:
        user = self.db.users.find_one({'user_id': user_id})
        if user:
            chat_state = user.get('chat_state')
            return ChatState[chat_state] if chat_state else None
        return None

    def update_user_properties(self, user_id: int, values: List[Tuple[str, Union[str, None]]]) -> None:
        self.db.users.update_one(
            {'user_id': user_id},
            {'$set': {key: value for key, value in values}},
            upsert=True
        )

    def get_users(self):
        for user in self.db.users.find({'chat_state': ChatState.HasAccess.name}):
            yield user


class UserBase:
    _db_name = None

    def __init__(self, user_id: Optional[int] = None):
        self._db = None
        self._pend_update = []

        self.user_id: int = None
        if user_id is not None:
            self.user_id = user_id

        self.national_id: str = None
        self.username: str = None
        self.chat_state: str = None
        self.chat_id: int = None
        self.otp_code: int = None
        self.captcha_id: int = None
        self.updated_at: int = None
        self.created_at: int = None
        self.referral: str = None
        self.agent_code: str = None

        self.trial_noticed: bool = None
        self.trial_ended: bool = None
        self.level: str = None
        self.level_checked_at: int = None
        self.channels: List[int] = None

        self.registration_wizard_step: int = None
        self.capital_limit: str = None

        self._loaded = False

    @property
    def db(self):
        if self._db is None:
            client = MongoClient(**rxconfig.MONGO_CONFIG)
            self._db = client[self._db_name]

        return self._db

    def _get_filter(self):
        if self.user_id:
            return {'user_id': self.user_id}

        raise Exception('!!!!! user id not assigned !!!!!')

    def _get_user(self):
        filter_ = self._get_filter()
        data = self.db.users.find_one(filter_)
        if data is not None:
            self.user_id = data.get('user_id')
            self.national_id = data.get('national_id')
            self.username = data.get('username')
            self.chat_state = data.get('chat_state')
            self.chat_id = data.get('chat_id')
            self.otp_code = data.get('otp_code')
            self.captcha_id = data.get('captcha_id')
            self.updated_at = data.get('updated_at')
            self.created_at = data.get('created_at')

            self.referral = data.get('referral')
            self.agent_code = data.get('agent_code')
            self.trial_ended = data.get('trial_ended')
            self.trial_noticed = data.get('trial_noticed')
            self.level = data.get('level')
            self.level_checked_at = data.get('level_checked_at')
            self.channels = data.get('channels')
            self.registration_wizard_step = data.get('registration_wizard_step')
            self.capital_limit = data.get('capital_limit')

        self._loaded = True
        return data

    def get(self):
        self._get_user()
        return self

    def get_user_by_national_id(self, national_id):
        data = self.db.users.find_one({'national_id': national_id})
        if data is None:
            self._loaded = True
            return self
        self.user_id = data['user_id']
        return self.get()

    def exists(self):
        if self._loaded is False:
            self._get_user()
        return bool(self.chat_id)

    def has_access(self):
        if self._loaded is False:
            self._get_user()
        return self.chat_state in [ChatState.HasAccess.name, ChatState.HasManualAccess.name]

    def get_chat_state(self) -> Union[ChatState, None]:
        if self._loaded is False:
            self._get_user()
        return ChatState[self.chat_state] if self.chat_state else None

    def delete(self):
        self.db.users.delete_one(self._get_filter())

    def upsert(self):
        if len(self._pend_update) == 0:
            return

        data = {attr: value for attr, value in self._pend_update}
        data['updated_at'] = int(datetime.datetime.now().timestamp())

        self.db.users.update_one(
            self._get_filter(),
            {'$set': data},
            upsert=True
        )
        self._pend_update = []

    def _update_channels(self):
        data = {'channels': list(set(self.channels))}
        data['updated_at'] = int(datetime.datetime.now().timestamp())

        self.db.users.update_one(
            self._get_filter(),
            {'$set': data},
            upsert=True
        )

    def add_channel(self, channel_id):
        if self._loaded is False:
            self._get_user()

        if self.channels is None:
            self.channels = []

        self.channels.append(channel_id)
        self._update_channels()

    def remove_channel(self, channel_id):
        if self._loaded is False:
            self._get_user()

        if self.channels is not None:
            new_channels = []
            for ch in self.channels:
                if ch != channel_id:
                    new_channels.append(ch)

            self.channels = new_channels
            self._update_channels()

    def __setattr__(self, attr, value):
        super().__setattr__(attr, value)

        if attr not in [
            'user_id', 'national_id', 'username', 'chat_state', 'chat_id', 'otp_code', 'captcha_id',
            'referral', 'level', 'created_at', 'level_checked_at', 'trial_ended', 'agent_code',
            'registration_wizard_step', 'capital_limit', 'trial_noticed'
        ]:
            return
        if isinstance(value, ChatState):
            value = value.name
        self._pend_update.append((attr, value))

    @property
    def joined_count(self):
        if self._loaded is False:
            self._get_user()

        return len(self.channels or [])

    def list_approved(self, condition):
        for user in self.db.users.find(condition):
            user = UserBase(user.get('user_id'))
            user._db_name = self._db_name
            user.get()
            yield user
