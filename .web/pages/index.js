/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Badge as RadixThemesBadge, Box as RadixThemesBox, Button as RadixThemesButton, Card as RadixThemesCard, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Grid as RadixThemesGrid, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Select as RadixThemesSelect, Table as RadixThemesTable, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { ArrowDownAZ as LucideArrowDownAZ, ArrowDownZA as LucideArrowDownZA, BarChart2 as LucideBarChart2, BarChartHorizontalBig as LucideBarChartHorizontalBig, Calendar as LucideCalendar, ChevronLeft as LucideChevronLeft, ChevronRight as LucideChevronRight, ChevronsLeft as LucideChevronsLeft, ChevronsRight as LucideChevronsRight, Cog as LucideCog, CreditCard as LucideCreditCard, Fingerprint as LucideFingerprint, Link as LucideLink, LogOut as LucideLogOut, Moon as LucideMoon, Rss as LucideRss, Search as LucideSearch, SquarePen as LucideSquarePen, Sun as LucideSun, Table2 as LucideTable2, Trash2 as LucideTrash2, User as LucideUser, UserCog as LucideUserCog, Users as LucideUsers, UserX as LucideUserX } from "lucide-react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getRefValue, getRefValues, isNotNullOrUndefined, isTrue } from "$/utils/state"
import { DynamicIcon } from "lucide-react/dynamic"
import { DebounceInput } from "react-debounce-input"
import { Control as RadixFormControl, Field as RadixFormField, Label as RadixFormLabel, Root as RadixFormRoot, Submit as RadixFormSubmit } from "@radix-ui/react-form"
import NextHead from "next/head"
import { jsx } from "@emotion/react"



export function Button_b8261bb782eb24045491d9d26b181b7a () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_b9b4602e20d45ff2d9c8652f1e060ac9 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.copy_invite_link", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{color:"blue",css:({ ["marginRight"] : "1em" }),onClick:on_click_b9b4602e20d45ff2d9c8652f1e060ac9,size:"2",variant:"soft"},
jsx(LucideLink,{css:({ ["marginRight"] : "0.25em" }),size:16},)
,"\u062f\u0631\u06cc\u0627\u0641\u062a \u0644\u06cc\u0646\u06a9 \u062f\u0639\u0648\u062a"
,)
  )
}

export function Button_fb21be5fdddf7a75a5eb71fbadf4f3fa () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_eba19eabfd586cac9879ec0a5a78cbe6 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.handle_logout", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{color:"red",onClick:on_click_eba19eabfd586cac9879ec0a5a78cbe6,size:"2",variant:"soft"},
jsx(LucideLogOut,{size:18},)
,"\u062e\u0631\u0648\u062c"
,)
  )
}

export function Fragment_f7955a91320509eab718dfeb22dfa9a4 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (jsx(
Fragment,
{},
jsx(Button_b8261bb782eb24045491d9d26b181b7a,{},)
,)) : (jsx(
Fragment,
{},
jsx(
RadixThemesText,
{as:"p"},
""
,),))),)
  )
}

export function Arrowdownaz_620348540ca79dd2d219ecb1061151db () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_696ff8af7fb0fe7f1552d13a297c902b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(LucideArrowDownAZ,{css:({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer" }),onClick:on_click_696ff8af7fb0fe7f1552d13a297c902b,size:28},)

  )
}

export function Iconbutton_890e36e647ed09dddb2590861e77fb6f () {
  
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])



  
  return (
    jsx(
RadixThemesIconButton,
{css:({ ["padding"] : "6px", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) }),onClick:on_click_9922dd3e837b9e087c86a2522c2c93f8,size:"2"},
jsx(Fragment_4735041bcb8d807a384b59168d698006,{},)
,)
  )
}

export function Select__root_50c76a7a6e9105c4914c07ae03afe676 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_dd4bff3eb042e1b3d4217b5fcfff2529 = useCallback(((_ev_0) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.sort_values", ({ ["sort_by"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesSelect.Root,
{defaultValue:reflex___state____state__customer_data___backend___backend____state.sort_value,name:"sort_selector",onValueChange:on_change_dd4bff3eb042e1b3d4217b5fcfff2529,size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0645\u0631\u062a\u0628\u200c\u0633\u0627\u0632\u06cc \u0628\u0631 \u0627\u0633\u0627\u0633..."},)
,jsx(
RadixThemesSelect.Content,
{},
jsx(
RadixThemesSelect.Item,
{value:"created_at_ts"},
"\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a"
,),jsx(
RadixThemesSelect.Item,
{value:"username"},
"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"
,),jsx(
RadixThemesSelect.Item,
{value:"national_id"},
"\u06a9\u062f \u0645\u0644\u06cc"
,),jsx(
RadixThemesSelect.Item,
{value:"raw_chat_state"},
"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"
,),jsx(
RadixThemesSelect.Item,
{value:"level"},
"\u0633\u0637\u062d"
,),jsx(
RadixThemesSelect.Item,
{value:"channel_count"},
"\u062a\u0639\u062f\u0627\u062f \u06a9\u0627\u0646\u0627\u0644"
,),),)
  )
}

export function Grid_4cd2f5099946701e1a21550f31103c01 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesGrid,
{columns:({ ["initial"] : "1", ["sm"] : "2", ["md"] : "2", ["lg"] : "4", ["xl"] : "5" }),css:({ ["width"] : "100%", ["alignItems"] : "stretch", ["paddingTop"] : "0.5em", ["paddingBottom"] : "0.5em" }),gap:"3"},
jsx(
RadixThemesCard,
{css:({ ["height"] : "100%", ["width"] : "100%" }),size:"3"},
jsx(
RadixThemesFlex,
{css:({ ["alignItems"] : "start", ["width"] : "100%" }),justify:"between",gap:"4"},
jsx(
RadixThemesBadge,
{color:"grass",css:({ ["padding"] : "0.65rem" }),highContrast:true,radius:"full",variant:"surface"},
jsx(LucideUsers,{css:({ ["color"] : "var(--grass-11)" }),size:28},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"column",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "var(--gray-11)" }),size:"3",weight:"medium"},
"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646 \u0634\u0645\u0627"
,),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesText,
{as:"p"},
""
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "end" }),direction:"row",gap:"2"},
jsx(Heading_0c35486247ba96a6882b7bf86939735a,{},)
,jsx(
RadixThemesText,
{as:"p"},
""
,),),),),),jsx(
RadixThemesCard,
{css:({ ["height"] : "100%", ["width"] : "100%" }),size:"3"},
jsx(
RadixThemesFlex,
{css:({ ["alignItems"] : "start", ["width"] : "100%" }),justify:"between",gap:"4"},
jsx(
RadixThemesBadge,
{color:"cyan",css:({ ["padding"] : "0.65rem" }),highContrast:true,radius:"full",variant:"surface"},
jsx(LucideRss,{css:({ ["color"] : "var(--cyan-11)" }),size:28},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"column",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "var(--gray-11)" }),size:"3",weight:"medium"},
"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646 \u0639\u0636\u0648 \u06a9\u0627\u0646\u0627\u0644"
,),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesText,
{as:"p"},
""
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "end" }),direction:"row",gap:"2"},
jsx(Heading_3a27abd35417495cde31a6516d4751f3,{},)
,jsx(
RadixThemesText,
{as:"p"},
""
,),),),),),reflex___state____state__customer_data___backend___auth_state____auth_state.allowed_levels_for_current_referral.map((level_key,index_1918d167ab604884)=>(jsx(
Fragment,
{key:index_1918d167ab604884},
(!((level_key === "_NO_LEVEL_")) ? (jsx(
Fragment,
{},
jsx(
RadixThemesCard,
{css:({ ["height"] : "100%", ["width"] : "100%" }),size:"3"},
jsx(
RadixThemesFlex,
{css:({ ["alignItems"] : "start", ["width"] : "100%" }),justify:"between",gap:"4"},
jsx(
RadixThemesBadge,
{color:((level_key === "level_1") ? "blue" : ((level_key === "level_2") ? "orange" : ((level_key === "level_golden") ? "yellow" : "purple"))),css:({ ["padding"] : "0.65rem" }),highContrast:true,radius:"full",variant:"surface"},
jsx(DynamicIcon,{css:({ ["size"] : 28, ["color"] : ("var(--"+((level_key === "level_1") ? "blue" : ((level_key === "level_2") ? "orange" : ((level_key === "level_golden") ? "yellow" : "purple")))+"-11)") }),name:((level_key === "level_1") ? "user-round-check" : ((level_key === "level_2") ? "user-round-cog" : ((level_key === "level_golden") ? "gem" : "award"))).replaceAll("_", "-")},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"column",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},
jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "var(--gray-11)" }),size:"3",weight:"medium"},
level_key.replaceAll("level_", "\u0633\u0637\u062d ")
,),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesText,
{as:"p"},
""
,),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "end" }),direction:"row",gap:"2"},
jsx(
RadixThemesHeading,
{size:"7",weight:"bold"},
((JSON.stringify((isTrue(reflex___state____state__customer_data___backend___backend____state.user_counts_by_level_var[level_key]) ? reflex___state____state__customer_data___backend___backend____state.user_counts_by_level_var[level_key] : 0)))+" \u06a9\u0627\u0631\u0628\u0631")
,),jsx(
RadixThemesText,
{as:"p"},
""
,),),),),),)) : (jsx(Fragment,{},)
)),))),)
  )
}

export function Arrowdownza_5023b0fad64ea8c28db2270cbfd87eb3 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_696ff8af7fb0fe7f1552d13a297c902b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(LucideArrowDownZA,{css:({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer" }),onClick:on_click_696ff8af7fb0fe7f1552d13a297c902b,size:28},)

  )
}

export function Button_7b171de2c24930389d6fc61aad40ce31 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_4fbf774ab2917adff5ed90557f633c02 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.next_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{disabled:(reflex___state____state__customer_data___backend___backend____state.current_page_number >= reflex___state____state__customer_data___backend___backend____state.total_pages),onClick:on_click_4fbf774ab2917adff5ed90557f633c02,size:"2",variant:"outline"},
"\u0628\u0639\u062f\u06cc"
,jsx(LucideChevronRight,{},)
,)
  )
}

export function Button_b05d82256c0ae3d4a30aad0fb0a02a57 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_51cff74557c24a3df454f28892d1cb8a = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.last_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{disabled:(reflex___state____state__customer_data___backend___backend____state.current_page_number >= reflex___state____state__customer_data___backend___backend____state.total_pages),onClick:on_click_51cff74557c24a3df454f28892d1cb8a,size:"2",variant:"outline"},
"\u0622\u062e\u0631\u06cc\u0646"
,jsx(LucideChevronsRight,{},)
,)
  )
}

export function Fragment_194f049d06c76496e21163f11c77639d () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (jsx(
Fragment,
{},
jsx(Button_fb21be5fdddf7a75a5eb71fbadf4f3fa,{},)
,)) : (jsx(Fragment,{},)
)),)
  )
}

export function Table__body_e4f42ad3ef805170d8753fd681d80a40 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)

  
    const handleSubmit_4a3101b7e8deb877c8352cf18ab695b2 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.update_customer_to_db", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))(ev));

        if (false) {
            $form.reset()
        }
    })
    




  
  return (
    jsx(
RadixThemesTable.Body,
{},
reflex___state____state__customer_data___backend___backend____state.paginated_users.map((user,index_682d9270aae5d2f6)=>(jsx(
RadixThemesTable.Row,
{align:"center",css:({ ["&:hover"] : ({ ["background"] : "var(--gray-3)" }) }),key:index_682d9270aae5d2f6},
jsx(
RadixThemesTable.Cell,
{},
(isTrue(user["username"]) ? user["username"] : "-")
,),jsx(
RadixThemesTable.Cell,
{},
(isTrue(user["national_id"]) ? user["national_id"] : "-")
,),jsx(
RadixThemesTable.Cell,
{},
(isTrue(user["chat_state_fa"]) ? user["chat_state_fa"] : (isTrue(user["raw_chat_state"]) ? user["raw_chat_state"] : "-"))
,),jsx(
RadixThemesTable.Cell,
{},
((isNotNullOrUndefined((isTrue(user["level"]) ? user["level"] : null)) && !(((isTrue(user["level"]) ? user["level"] : null) === ""))) ? (((isTrue(user["level"]) ? user["level"] : null) === "_NO_LEVEL_") ? "-" : (isTrue(user["level"]) ? user["level"] : null).replaceAll("level_", "")) : "-")
,),jsx(
RadixThemesTable.Cell,
{},
(isTrue(user["created_at_str"]) ? user["created_at_str"] : "-")
,),jsx(
RadixThemesTable.Cell,
{},
jsx(
Fragment,
{},
(((isTrue(user["channel_count"]) ? user["channel_count"] : 0) > 0) ? (jsx(
Fragment,
{},
jsx(
RadixThemesBadge,
{color:"grass",radius:"full",size:"2",variant:"soft"},
jsx(LucideUsers,{size:16},)
,(("\u0639\u0636\u0648 \u062f\u0631 "+(JSON.stringify((isTrue(user["channel_count"]) ? user["channel_count"] : 0))))+" \u06a9\u0627\u0646\u0627\u0644")
,),)) : (jsx(
Fragment,
{},
jsx(
RadixThemesBadge,
{color:"tomato",radius:"full",size:"2",variant:"soft"},
jsx(LucideUserX,{size:16},)
,"\u0639\u0636\u0648 \u0646\u06cc\u0633\u062a"
,),))),),),jsx(
RadixThemesTable.Cell,
{},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(
RadixThemesDialog.Root,
{},
jsx(
RadixThemesDialog.Trigger,
{},
jsx(
RadixThemesFlex,
{},
jsx(
RadixThemesButton,
{color:"blue",disabled:((isTrue(user["_id_str"]) ? user["_id_str"] : "") === ""),onClick:((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.set_current_user_for_edit", ({ ["object_id_str"] : (isTrue(user["_id_str"]) ? user["_id_str"] : "") }), ({  })))], args, ({  })))),size:"2",variant:"solid"},
jsx(LucideSquarePen,{size:22},)
,jsx(
RadixThemesText,
{as:"p",size:"3"},
"\u0648\u06cc\u0631\u0627\u06cc\u0634"
,),),),),jsx(
RadixThemesDialog.Content,
{css:({ ["maxWidth"] : "450px", ["padding"] : "1.5em", ["border"] : "2px solid var(--accent-7)", ["borderRadius"] : "25px" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["height"] : "100%", ["marginBottom"] : "1.5em", ["alignItems"] : "center", ["width"] : "100%" }),direction:"row",gap:"4"},
jsx(
RadixThemesBadge,
{color:"grass",css:({ ["padding"] : "0.65rem" }),radius:"full"},
jsx(LucideSquarePen,{size:34},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["height"] : "100%", ["alignItems"] : "start" }),direction:"column",gap:"1"},
jsx(
RadixThemesDialog.Title,
{css:({ ["weight"] : "bold", ["margin"] : "0" })},
"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0631"
,),jsx(
RadixThemesDialog.Description,
{},
"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u0628\u0631 \u0631\u0627 \u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0646\u06cc\u062f"
,),),),jsx(
RadixThemesFlex,
{css:({ ["width"] : "100%" }),direction:"column",gap:"4"},
jsx(
Fragment,
{},
(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (jsx(
Fragment,
{},
jsx(
RadixFormRoot,
{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_4a3101b7e8deb877c8352cf18ab695b2},
jsx(
RadixThemesFlex,
{direction:"column",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%", ["marginBottom"] : "0.75em" }),direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",direction:"row",gap:"3"},
jsx(LucideFingerprint,{size:16},)
,jsx(
RadixThemesText,
{as:"p",weight:"medium"},
"\u0634\u0646\u0627\u0633\u0647 \u062f\u0627\u062e\u0644\u06cc (\u0641\u0642\u0637 \u062e\u0648\u0627\u0646\u062f\u0646\u06cc)"
,),),jsx(RadixThemesTextField.Root,{css:({ ["width"] : "100%" }),disabled:true,value:(isNotNullOrUndefined((isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "") : "")) ? (isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "") : "") : "")},)
,),jsx(
RadixFormField,
{className:"Field ",css:({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%" }),name:"username"},
jsx(
RadixThemesFlex,
{direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUser,{css:({ ["strokeWidth"] : 1.5 }),size:16},)
,jsx(
RadixFormLabel,
{className:"Label ",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })},
"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"
,),),jsx(
RadixFormControl,
{asChild:true,className:"Control "},
jsx(RadixThemesTextField.Root,{defaultValue:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"] : "") : ""),name:"username",placeholder:"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc",required:true,type:"text"},)
,),),),jsx(
RadixFormField,
{className:"Field ",css:({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%" }),name:"national_id"},
jsx(
RadixThemesFlex,
{direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideCreditCard,{css:({ ["strokeWidth"] : 1.5 }),size:16},)
,jsx(
RadixFormLabel,
{className:"Label ",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })},
"\u06a9\u062f \u0645\u0644\u06cc"
,),),jsx(
RadixFormControl,
{asChild:true,className:"Control "},
jsx(RadixThemesTextField.Root,{defaultValue:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"] : "") : ""),name:"national_id",placeholder:"\u06a9\u062f \u0645\u0644\u06cc (\u0627\u062e\u062a\u06cc\u0627\u0631\u06cc)",required:false,type:"text"},)
,),),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUserCog,{css:({ ["strokeWidth"] : 1.5 }),size:16},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"
,),),jsx(
RadixThemesSelect.Root,
{css:({ ["width"] : "100%" }),defaultValue:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"] : "HasAccess") : "HasAccess"),name:"chat_state",size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0627\u0646\u062a\u062e\u0627\u0628 \u0648\u0636\u0639\u06cc\u062a..."},)
,jsx(
RadixThemesSelect.Content,
{},
jsx(
RadixThemesSelect.Item,
{value:"HasAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0627\u0631\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"HasManualAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0633\u062a\u06cc \u062f\u0627\u0631\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"INITED"},
"\u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"BLOCKED"},
"\u0645\u0633\u062f\u0648\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"WaitForNationalId"},
"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u062f\u0645\u0644\u06cc"
,),jsx(
RadixThemesSelect.Item,
{value:"WaitForOTP"},
"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"WaitForCaptcha"},
"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u067e\u0686\u0627"
,),jsx(
RadixThemesSelect.Item,
{value:"LoggedIn"},
"\u0644\u0627\u06af\u06cc\u0646 \u0634\u062f\u0647"
,),),),),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"1"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideBarChart2,{css:({ ["strokeWidth"] : 1.5 }),size:16},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0633\u0637\u062d \u06a9\u0627\u0631\u0628\u0631"
,),),jsx(
RadixThemesSelect.Root,
{css:({ ["width"] : "100%" }),defaultValue:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["level"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["level"] : "_NO_LEVEL_") : "_NO_LEVEL_"),name:"level",size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0627\u0646\u062a\u062e\u0627\u0628 \u0633\u0637\u062d..."},)
,jsx(
RadixThemesSelect.Content,
{},
reflex___state____state__customer_data___backend___auth_state____auth_state.level_options_for_dropdown.map((opt,index_09a67295b0aae870)=>(jsx(
RadixThemesSelect.Item,
{key:index_09a67295b0aae870,value:opt.at(1)},
opt.at(0)
,))),),),),),jsx(
RadixThemesFlex,
{css:({ ["paddingTop"] : "2em", ["mt"] : "4" }),justify:"end",gap:"3"},
jsx(
RadixThemesDialog.Close,
{},
jsx(
RadixThemesFlex,
{},
jsx(
RadixThemesButton,
{color:"gray",onClick:((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.clear_current_user_for_edit", ({  }), ({  })))], args, ({  })))),variant:"soft"},
"\u0644\u063a\u0648"
,),),),jsx(
RadixFormSubmit,
{asChild:true,className:"Submit "},
jsx(
RadixThemesDialog.Close,
{},
jsx(
RadixThemesButton,
{},
"\u0628\u0647\u200c\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc \u06a9\u0627\u0631\u0628\u0631"
,),),),),),)) : (jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "200px" })},
jsx(
RadixThemesText,
{as:"p"},
"\u06a9\u0627\u0631\u0628\u0631\u06cc \u0628\u0631\u0627\u06cc \u0648\u06cc\u0631\u0627\u06cc\u0634 \u0627\u0646\u062a\u062e\u0627\u0628 \u0646\u0634\u062f\u0647 \u06cc\u0627 \u062f\u0631 \u062d\u0627\u0644 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc \u0627\u0633\u062a..."
,),),))),),),),),jsx(
RadixThemesIconButton,
{color:"red",css:({ ["padding"] : "6px" }),disabled:((isTrue(user["_id_str"]) ? user["_id_str"] : "") === ""),onClick:((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.delete_customer", ({ ["object_id_str"] : (isTrue(user["_id_str"]) ? user["_id_str"] : "") }), ({  })))], args, ({  })))),size:"2",variant:"solid"},
jsx(LucideTrash2,{size:24},)
,),),),))),)
  )
}

export function Fragment_4735041bcb8d807a384b59168d698006 () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)





  
  return (
    jsx(
Fragment,
{},
((resolvedColorMode === "light") ? (jsx(
Fragment,
{},
jsx(LucideSun,{},)
,)) : (jsx(
Fragment,
{},
jsx(LucideMoon,{},)
,))),)
  )
}

export function Text_01904e52bdfab360cadbf71a7e12398c () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesText,
{as:"p",size:"3"},
"\u0635\u0641\u062d\u0647 "
,(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.current_page_number))
," \u0627\u0632 "
,(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.total_pages))
,)
  )
}

export function Fragment_6da3603dc64deef17c75aeacfa268b83 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__customer_data___backend___backend____state.sort_reverse ? (jsx(
Fragment,
{},
jsx(Arrowdownza_5023b0fad64ea8c28db2270cbfd87eb3,{},)
,)) : (jsx(
Fragment,
{},
jsx(Arrowdownaz_620348540ca79dd2d219ecb1061151db,{},)
,))),)
  )
}

export function Button_1cc124ab2bb8e95f566e63ab70fb8845 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_b139ef4aa1672e906adee41edbb5678b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.first_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{disabled:(reflex___state____state__customer_data___backend___backend____state.current_page_number <= 1),onClick:on_click_b139ef4aa1672e906adee41edbb5678b,size:"2",variant:"outline"},
jsx(LucideChevronsLeft,{},)
,"\u0627\u0648\u0644\u06cc\u0646"
,)
  )
}

export function Heading_0c35486247ba96a6882b7bf86939735a () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesHeading,
{size:"7",weight:"bold"},
((JSON.stringify(reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral))+" \u06a9\u0627\u0631\u0628\u0631")
,)
  )
}

export function Debounceinput_1966cc3c87a310296e4ec46085c5d718 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_6c5ff3d4049341dd3eb403ab81e47aa8 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.filter_values", ({ ["search_term"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(
DebounceInput,
{css:({ ["maxWidth"] : "225px", ["width"] : "100%" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_6c5ff3d4049341dd3eb403ab81e47aa8,placeholder:"\u062c\u0633\u062a\u062c\u0648\u06cc \u06a9\u0627\u0631\u0628\u0631\u0627\u0646...",size:"3",value:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.search_value) ? reflex___state____state__customer_data___backend___backend____state.search_value : ""),variant:"surface"},
jsx(
RadixThemesTextField.Slot,
{},
jsx(LucideSearch,{},)
,),)
  )
}

export function Heading_3a27abd35417495cde31a6516d4751f3 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesHeading,
{size:"7",weight:"bold"},
((JSON.stringify(reflex___state____state__customer_data___backend___backend____state.users_in_channels_count_var))+" \u0646\u0641\u0631")
,)
  )
}

export function Button_23ea60e1ebc38918d73c5d28b39a1363 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_e286d0bd833f8c44452e8d142cc033ab = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.prev_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesButton,
{disabled:(reflex___state____state__customer_data___backend___backend____state.current_page_number <= 1),onClick:on_click_e286d0bd833f8c44452e8d142cc033ab,size:"2",variant:"outline"},
jsx(LucideChevronLeft,{},)
,"\u0642\u0628\u0644\u06cc"
,)
  )
}

export default function Component() {
    




  return (
    jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["@media screen and (min-width: 0)"] : ({ ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em" }), ["@media screen and (min-width: 30em)"] : ({ ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em" }), ["@media screen and (min-width: 48em)"] : ({ ["paddingInlineStart"] : "3em", ["paddingInlineEnd"] : "3em" }), ["paddingBottom"] : "2em" }),direction:"column",gap:"6"},
jsx(
RadixThemesFlex,
{align:"center",css:({ ["@media screen and (min-width: 0)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 30em)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 48em)"] : ({ ["flexDirection"] : "row" }), ["width"] : "100%", ["top"] : "0px", ["paddingTop"] : "1em", ["paddingBottom"] : "1em", ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em", ["borderBottom"] : "1px solid var(--gray-a5)", ["background"] : "var(--gray-1)" }),gap:"2"},
jsx(
RadixThemesBadge,
{color:"green",css:({ ["align"] : "center", ["padding"] : "0.65rem" }),radius:"large",variant:"surface"},
jsx(LucideTable2,{size:28},)
,jsx(
RadixThemesHeading,
{css:({ ["direction"] : "rtl" }),size:"6"},
"\u067e\u0646\u0644 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646"
,),),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"3"},
jsx(Fragment_f7955a91320509eab718dfeb22dfa9a4,{},)
,jsx(Iconbutton_890e36e647ed09dddb2590861e77fb6f,{},)
,jsx(Fragment_194f049d06c76496e21163f11c77639d,{},)
,),),jsx(Grid_4cd2f5099946701e1a21550f31103c01,{},)
,jsx(
RadixThemesBox,
{css:({ ["width"] : "100%" })},
jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{align:"center",css:({ ["width"] : "100%", ["paddingBottom"] : "1em" }),justify:"end",gap:"3",wrap:"wrap"},
jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(Fragment_6da3603dc64deef17c75aeacfa268b83,{},)
,jsx(Select__root_50c76a7a6e9105c4914c07ae03afe676,{},)
,jsx(Debounceinput_1966cc3c87a310296e4ec46085c5d718,{},)
,),jsx(
RadixThemesTable.Root,
{css:({ ["width"] : "100%" }),size:"3",variant:"surface"},
jsx(
RadixThemesTable.Header,
{},
jsx(
RadixThemesTable.Row,
{},
jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUser,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideCreditCard,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u06a9\u062f \u0645\u0644\u06cc"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUserCog,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideBarChartHorizontalBig,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0633\u0637\u062d"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideCalendar,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUsers,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0648\u0636\u0639\u06cc\u062a \u0639\u0636\u0648\u06cc\u062a"
,),),),jsx(
RadixThemesTable.ColumnHeaderCell,
{},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideCog,{size:18},)
,jsx(
RadixThemesText,
{as:"p"},
"\u0639\u0645\u0644\u06cc\u0627\u062a"
,),),),),),jsx(Table__body_e4f42ad3ef805170d8753fd681d80a40,{},)
,),jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",css:({ ["width"] : "100%", ["paddingTop"] : "1em", ["paddingBottom"] : "1em" }),direction:"row",justify:"center",gap:"3"},
jsx(Button_1cc124ab2bb8e95f566e63ab70fb8845,{},)
,jsx(Button_23ea60e1ebc38918d73c5d28b39a1363,{},)
,jsx(Text_01904e52bdfab360cadbf71a7e12398c,{},)
,jsx(Button_7b171de2c24930389d6fc61aad40ce31,{},)
,jsx(Button_b05d82256c0ae3d4a30aad0fb0a02a57,{},)
,),),),),jsx(
NextHead,
{},
jsx(
"title",
{},
"\u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,),)
  )
}
