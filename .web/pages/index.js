/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Badge as RadixThemesBadge, Box as RadixThemesBox, Button as RadixThemesButton, Card as RadixThemesCard, Code as RadixThemesCode, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Heading as RadixThemesHeading, IconButton as RadixThemesIconButton, Link as RadixThemesLink, Select as RadixThemesSelect, Table as RadixThemesTable, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { ArrowDownAZ as LucideArrowDownAZ, ArrowDownZA as LucideArrowDownZA, Calendar as LucideCalendar, ChevronLeft as LucideChevronLeft, ChevronRight as LucideChevronRight, ChevronsLeft as LucideChevronsLeft, ChevronsRight as LucideChevronsRight, Cog as LucideCog, CreditCard as LucideCreditCard, Fingerprint as LucideFingerprint, LogOut as LucideLogOut, Moon as LucideMoon, Plus as LucidePlus, Search as LucideSearch, SquarePen as LucideSquarePen, Sun as LucideSun, Table2 as LucideTable2, Trash2 as LucideTrash2, User as LucideUser, UserCog as LucideUserCog, Users as LucideUsers, UserX as LucideUserX } from "lucide-react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getRefValue, getRefValues, isNotNullOrUndefined, isTrue } from "$/utils/state"
import NextLink from "next/link"
import { DynamicIcon } from "lucide-react/dynamic"
import { Control as RadixFormControl, Field as RadixFormField, Label as RadixFormLabel, Root as RadixFormRoot, Submit as RadixFormSubmit } from "@radix-ui/react-form"
import { DebounceInput } from "react-debounce-input"
import NextHead from "next/head"
import { jsx } from "@emotion/react"



export function Link_6d8ef781efad3969e1ad202c69c43883 () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)





  
  return (
    jsx(
RadixThemesLink,
{asChild:true,css:({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) }),size:"3"},
jsx(
NextLink,
{href:"https://reflex.dev",passHref:true},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",css:({ ["textAlign"] : "center", ["padding"] : "1em" }),direction:"row",gap:"3"},
"Built with "
,jsx(
"svg",
{"aria-label":"Reflex",css:({ ["fill"] : ((resolvedColorMode === "light") ? "#110F1F" : "white") }),height:"12",role:"img",width:"56",xmlns:"http://www.w3.org/2000/svg"},
jsx("path",{d:"M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z"},)
,jsx("path",{d:"M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z"},)
,jsx("path",{d:"M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z"},)
,jsx("path",{d:"M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z"},)
,jsx("path",{d:"M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z"},)
,jsx("path",{d:"M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z"},)
,jsx(
"title",
{},
"Reflex"
,),),),),)
  )
}

export function Arrowdownza_5023b0fad64ea8c28db2270cbfd87eb3 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_696ff8af7fb0fe7f1552d13a297c902b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(LucideArrowDownZA,{css:({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer" }),onClick:on_click_696ff8af7fb0fe7f1552d13a297c902b,size:28},)

  )
}

export function Select__root_c889fd9b05af1b2da5bffe2cdaad869e () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_dd4bff3eb042e1b3d4217b5fcfff2529 = useCallback(((_ev_0) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.sort_values", ({ ["sort_by"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, Event])



  
  return (
    jsx(
RadixThemesSelect.Root,
{defaultValue:"username",onValueChange:on_change_dd4bff3eb042e1b3d4217b5fcfff2529,size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0645\u0631\u062a\u0628\u200c\u0633\u0627\u0632\u06cc \u0628\u0631 \u0627\u0633\u0627\u0633: \u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"},)
,jsx(
RadixThemesSelect.Content,
{},
jsx(
RadixThemesSelect.Group,
{},
""
,jsx(
RadixThemesSelect.Item,
{value:"username"},
"username"
,),jsx(
RadixThemesSelect.Item,
{value:"national_id"},
"national_id"
,),jsx(
RadixThemesSelect.Item,
{value:"raw_chat_state"},
"raw_chat_state"
,),jsx(
RadixThemesSelect.Item,
{value:"created_at_str"},
"created_at_str"
,),jsx(
RadixThemesSelect.Item,
{value:"channel_count"},
"channel_count"
,),),),)
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

export function Iconbutton_98348b16bede352a0d51b6c9200c6e68 () {
  
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])



  
  return (
    jsx(
RadixThemesIconButton,
{css:({ ["padding"] : "6px", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) }),onClick:on_click_9922dd3e837b9e087c86a2522c2c93f8},
jsx(Fragment_4735041bcb8d807a384b59168d698006,{},)
,)
  )
}

export function Root_062a14c3c812109d8c7c01fa51415458 () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  
    const handleSubmit_9b32ec31bd09095566fea56cfe0c85c3 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.add_customer_to_db", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))(ev));

        if (true) {
            $form.reset()
        }
    })
    




  
  return (
    jsx(
RadixFormRoot,
{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_9b32ec31bd09095566fea56cfe0c85c3},
jsx(
RadixThemesFlex,
{direction:"column",gap:"3"},
jsx(
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
jsx(RadixThemesTextField.Root,{defaultValue:"",name:"username",placeholder:"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc",required:true,type:"text"},)
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
jsx(RadixThemesTextField.Root,{defaultValue:"",name:"national_id",placeholder:"\u06a9\u062f \u0645\u0644\u06cc (\u0627\u062e\u062a\u06cc\u0627\u0631\u06cc)",required:false,type:"text"},)
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
{css:({ ["width"] : "100%" }),defaultValue:"HasAccess",name:"chat_state",size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0627\u0646\u062a\u062e\u0627\u0628 \u0648\u0636\u0639\u06cc\u062a..."},)
,jsx(
RadixThemesSelect.Content,
{},
jsx(
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
,),jsx(
RadixThemesSelect.Item,
{value:"HasAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0627\u0631\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"HasManualAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0633\u062a\u06cc \u062f\u0627\u0631\u062f"
,),),),),),jsx(
RadixThemesFlex,
{css:({ ["paddingTop"] : "2em", ["mt"] : "4" }),justify:"end",gap:"3"},
jsx(
RadixThemesDialog.Close,
{},
jsx(
RadixThemesButton,
{color:"gray",variant:"soft"},
"\u0644\u063a\u0648"
,),),jsx(
RadixFormSubmit,
{asChild:true,className:"Submit "},
jsx(
RadixThemesDialog.Close,
{},
jsx(
RadixThemesButton,
{},
"\u062b\u0628\u062a \u06a9\u0627\u0631\u0628\u0631"
,),),),),)
  )
}

export function Badge_628cb5a3b8156e68b93902703dee1166 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesBadge,
{color:((reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral >= reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"]) ? "grass" : "tomato"),css:({ ["alignItems"] : "center" }),radius:"large"},
jsx(Dynamicicon_577278a6418503b95b6888b31febf615,{},)
,jsx(Text_68f423a34a70a35d77864e22c0903065,{},)
,)
  )
}

export function Table__body_dd71eeef806922c97444e7b2f019a327 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  
    const handleSubmit_3559348d9f9b4c3d8904790524c19e73 = useCallback((ev) => {
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
reflex___state____state__customer_data___backend___backend____state.paginated_users.map((user,index_81732205aff7e50e)=>(jsx(
RadixThemesTable.Row,
{align:"center",css:({ ["&:hover"] : ({ ["background"] : "var(--gray-3)" }) }),key:index_81732205aff7e50e},
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
(isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (jsx(
Fragment,
{},
jsx(
RadixFormRoot,
{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_3559348d9f9b4c3d8904790524c19e73},
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
,),),jsx(RadixThemesTextField.Root,{css:({ ["width"] : "100%" }),disabled:true,value:(isNotNullOrUndefined((isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "")) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "") : "")},)
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
jsx(RadixThemesTextField.Root,{defaultValue:(isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"] : ""),name:"username",placeholder:"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc",required:true,type:"text"},)
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
jsx(RadixThemesTextField.Root,{defaultValue:(isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"] : ""),name:"national_id",placeholder:"\u06a9\u062f \u0645\u0644\u06cc (\u0627\u062e\u062a\u06cc\u0627\u0631\u06cc)",required:false,type:"text"},)
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
{css:({ ["width"] : "100%" }),defaultValue:(isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"] : "HasAccess") : "HasAccess"),name:"chat_state",size:"3"},
jsx(RadixThemesSelect.Trigger,{placeholder:"\u0627\u0646\u062a\u062e\u0627\u0628 \u0648\u0636\u0639\u06cc\u062a..."},)
,jsx(
RadixThemesSelect.Content,
{},
jsx(
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
,),jsx(
RadixThemesSelect.Item,
{value:"HasAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0627\u0631\u062f"
,),jsx(
RadixThemesSelect.Item,
{value:"HasManualAccess"},
"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0633\u062a\u06cc \u062f\u0627\u0631\u062f"
,),),),),),jsx(
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
"..."
,),),))),),),),),jsx(
RadixThemesIconButton,
{color:"red",css:({ ["padding"] : "6px" }),disabled:((isTrue(user["_id_str"]) ? user["_id_str"] : "") === ""),onClick:((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.delete_customer", ({ ["object_id_str"] : (isTrue(user["_id_str"]) ? user["_id_str"] : "") }), ({  })))], args, ({  })))),size:"2",variant:"solid"},
jsx(LucideTrash2,{size:24},)
,),),),))),)
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

export function Arrowdownaz_620348540ca79dd2d219ecb1061151db () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_696ff8af7fb0fe7f1552d13a297c902b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    jsx(LucideArrowDownAZ,{css:({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer" }),onClick:on_click_696ff8af7fb0fe7f1552d13a297c902b,size:28},)

  )
}

export function Fragment_751db3a2c6d251f2e50e8ce28fa73d9b () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (jsx(
Fragment,
{},
jsx(
RadixThemesText,
{as:"p",css:({ ["marginRight"] : "1em" }),size:"3"},
"\u06a9\u062f \u0645\u0639\u0631\u0641: "
,jsx(Code_206d9ea80be907ffa6bf251f0dc82a0d,{},)
,),)) : (jsx(Fragment,{},)
)),)
  )
}

export function Dynamicicon_577278a6418503b95b6888b31febf615 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(DynamicIcon,{css:({ ["color"] : ("var(--"+((reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral >= reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"]) ? "grass" : "tomato")+"-9)") }),name:((reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral >= reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"]) ? "trending-up" : "trending-down").replaceAll("_", "-")},)

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

export function Code_206d9ea80be907ffa6bf251f0dc82a0d () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
RadixThemesCode,
{},
reflex___state____state__customer_data___backend___auth_state____auth_state.current_logged_in_referral
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

export function Fragment_7c8e7a16f8af8b77889dc8fd11597ad3 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
Fragment,
{},
(reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (jsx(
Fragment,
{},
jsx(Button_fb21be5fdddf7a75a5eb71fbadf4f3fa,{},)
,)) : (jsx(
Fragment,
{},
null
,))),)
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

export function Text_68f423a34a70a35d77864e22c0903065 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : ("var(--"+((reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral >= reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"]) ? "grass" : "tomato")+"-9)") }),size:"2",weight:"medium"},
((JSON.stringify(reflex___state____state__customer_data___backend___backend____state.customers_change))+"%")
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

export function Heading_4af665d50fa80aa92183c4e502c1c955 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesHeading,
{size:"7",weight:"bold"},
(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral))
,)
  )
}

export function Text_b92b796abfeef8a41e053231a59327c1 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "var(--gray-10)" }),size:"3"},
("\u0627\u0632 "+(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"])))
,)
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

export function Fragment_496a84fea9145b7e70494a16250f6205 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
Fragment,
{},
((reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"] !== 0) ? (jsx(
Fragment,
{},
jsx(Text_b92b796abfeef8a41e053231a59327c1,{},)
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

export function Fragment_e1c8283e1cd6173f1da7e3a906f13658 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    jsx(
Fragment,
{},
((((reflex___state____state__customer_data___backend___backend____state.previous_month_values["num_customers"] !== 0) && (reflex___state____state__customer_data___backend___backend____state.customers_change !== Infinity)) && (reflex___state____state__customer_data___backend___backend____state.customers_change !== -Infinity)) ? (jsx(
Fragment,
{},
jsx(Badge_628cb5a3b8156e68b93902703dee1166,{},)
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
{align:"center",css:({ ["@media screen and (min-width: 0)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 30em)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 48em)"] : ({ ["flexDirection"] : "row" }), ["width"] : "100%", ["top"] : "0px", ["paddingTop"] : "1em", ["paddingBottom"] : "1em", ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em", ["borderBottom"] : "1px solid var(--gray-a5)", ["background"] : "var(--gray-2)", ["position"] : "sticky", ["zIndex"] : "10" }),gap:"2"},
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
jsx(Fragment_751db3a2c6d251f2e50e8ce28fa73d9b,{},)
,jsx(
RadixThemesFlex,
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })},
jsx(Link_6d8ef781efad3969e1ad202c69c43883,{},)
,),jsx(Iconbutton_98348b16bede352a0d51b6c9200c6e68,{},)
,jsx(Fragment_7c8e7a16f8af8b77889dc8fd11597ad3,{},)
,),),jsx(
RadixThemesFlex,
{css:({ ["width"] : "100%", ["justifyContent"] : "center" }),gap:"5",wrap:"wrap"},
jsx(
RadixThemesCard,
{css:({ ["width"] : "100%", ["maxWidth"] : "22rem" }),size:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "start", ["width"] : "100%" }),direction:"column",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",justify:"between",gap:"3"},
jsx(
RadixThemesFlex,
{align:"center",className:"rx-Stack",direction:"row",gap:"2"},
jsx(LucideUsers,{css:({ ["color"] : "var(--blue-11)" }),size:22},)
,jsx(
RadixThemesText,
{as:"p",css:({ ["color"] : "var(--gray-11)" }),size:"4",weight:"medium"},
"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646 \u0645\u0639\u0631\u0641"
,),),jsx(Fragment_e1c8283e1cd6173f1da7e3a906f13658,{},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "end" }),direction:"row",gap:"2"},
jsx(Heading_4af665d50fa80aa92183c4e502c1c955,{},)
,jsx(Fragment_496a84fea9145b7e70494a16250f6205,{},)
,),),),),),jsx(
RadixThemesBox,
{css:({ ["width"] : "100%" })},
jsx(
Fragment,
{},
jsx(
RadixThemesFlex,
{align:"center",css:({ ["width"] : "100%", ["paddingBottom"] : "1em" }),justify:"end",gap:"3",wrap:"wrap"},
jsx(
RadixThemesDialog.Root,
{},
jsx(
RadixThemesDialog.Trigger,
{},
jsx(
RadixThemesButton,
{size:"3"},
jsx(LucidePlus,{size:26},)
,jsx(
RadixThemesText,
{as:"p",css:({ ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "block" }) }),size:"4"},
"\u0627\u0641\u0632\u0648\u062f\u0646 \u06a9\u0627\u0631\u0628\u0631"
,),),),jsx(
RadixThemesDialog.Content,
{css:({ ["maxWidth"] : "450px", ["padding"] : "1.5em", ["border"] : "2px solid var(--accent-7)", ["borderRadius"] : "25px" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["height"] : "100%", ["marginBottom"] : "1.5em", ["alignItems"] : "center", ["width"] : "100%" }),direction:"row",gap:"4"},
jsx(
RadixThemesBadge,
{color:"grass",css:({ ["padding"] : "0.65rem" }),radius:"full"},
jsx(LucideUsers,{size:34},)
,),jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["height"] : "100%", ["alignItems"] : "start" }),direction:"column",gap:"1"},
jsx(
RadixThemesDialog.Title,
{css:({ ["weight"] : "bold", ["margin"] : "0" })},
"\u0627\u0641\u0632\u0648\u062f\u0646 \u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f"
,),jsx(
RadixThemesDialog.Description,
{},
"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f \u0631\u0627 \u0648\u0627\u0631\u062f \u06a9\u0646\u06cc\u062f"
,),),),jsx(
RadixThemesFlex,
{css:({ ["width"] : "100%" }),direction:"column",gap:"4"},
jsx(Root_062a14c3c812109d8c7c01fa51415458,{},)
,),),),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},)
,jsx(Fragment_6da3603dc64deef17c75aeacfa268b83,{},)
,jsx(Select__root_c889fd9b05af1b2da5bffe2cdaad869e,{},)
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
,),),),),),jsx(Table__body_dd71eeef806922c97444e7b2f019a327,{},)
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
