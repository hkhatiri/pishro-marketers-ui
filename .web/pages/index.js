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



export function Grid_81454f8cc7102014a5f755589cbe32ec () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    <RadixThemesGrid columns={({ ["initial"] : "1", ["sm"] : "2", ["md"] : "2", ["lg"] : "4", ["xl"] : "5" })} css={({ ["width"] : "100%", ["alignItems"] : "stretch", ["paddingTop"] : "0.5em", ["paddingBottom"] : "0.5em" })} gap={"3"}>

<RadixThemesCard css={({ ["height"] : "100%", ["width"] : "100%" })} size={"3"}>

<RadixThemesFlex css={({ ["alignItems"] : "start", ["width"] : "100%" })} justify={"between"} gap={"4"}>

<RadixThemesBadge color={"grass"} css={({ ["padding"] : "0.65rem" })} highContrast={true} radius={"full"} variant={"surface"}>

<LucideUsers css={({ ["color"] : "var(--grass-11)" })} size={28}/>
</RadixThemesBadge>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "start", ["width"] : "100%" })} direction={"column"} justify={"between"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} justify={"between"} gap={"3"}>

<RadixThemesText as={"p"} css={({ ["color"] : "var(--gray-11)" })} size={"3"} weight={"medium"}>

{"\u062a\u0639\u062f\u0627\u062f \u06a9\u0644 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646 \u0634\u0645\u0627"}
</RadixThemesText>
<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "end" })} direction={"row"} gap={"2"}>

<Heading_f64f44e8d1ab5843f383890be6ee33a6/>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesCard>
<RadixThemesCard css={({ ["height"] : "100%", ["width"] : "100%" })} size={"3"}>

<RadixThemesFlex css={({ ["alignItems"] : "start", ["width"] : "100%" })} justify={"between"} gap={"4"}>

<RadixThemesBadge color={"cyan"} css={({ ["padding"] : "0.65rem" })} highContrast={true} radius={"full"} variant={"surface"}>

<LucideRss css={({ ["color"] : "var(--cyan-11)" })} size={28}/>
</RadixThemesBadge>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "start", ["width"] : "100%" })} direction={"column"} justify={"between"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} justify={"between"} gap={"3"}>

<RadixThemesText as={"p"} css={({ ["color"] : "var(--gray-11)" })} size={"3"} weight={"medium"}>

{"\u06a9\u0627\u0631\u0628\u0631\u0627\u0646 \u0639\u0636\u0648 \u06a9\u0627\u0646\u0627\u0644"}
</RadixThemesText>
<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "end" })} direction={"row"} gap={"2"}>

<Heading_c0325dca407252a4b40a0804e3d1a140/>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesCard>
<>{ reflex___state____state__customer_data___backend___auth_state____auth_state.allowed_levels_for_current_referral.map((level_key, index_8d98d6d5b5dedddc) => (
  <Fragment key={index_8d98d6d5b5dedddc}>

{!((level_key === "_NO_LEVEL_")) ? (
  <Fragment>

<RadixThemesCard css={({ ["height"] : "100%", ["width"] : "100%" })} size={"3"}>

<RadixThemesFlex css={({ ["alignItems"] : "start", ["width"] : "100%" })} justify={"between"} gap={"4"}>

<RadixThemesBadge color={((level_key === "level_1") ? "blue" : ((level_key === "level_2") ? "orange" : ((level_key === "level_golden") ? "yellow" : "purple")))} css={({ ["padding"] : "0.65rem" })} highContrast={true} radius={"full"} variant={"surface"}>

<DynamicIcon css={({ ["size"] : 28, ["color"] : ("var(--"+((level_key === "level_1") ? "blue" : ((level_key === "level_2") ? "orange" : ((level_key === "level_golden") ? "yellow" : "purple")))+"-11)") })} name={((level_key === "level_1") ? "user-round-check" : ((level_key === "level_2") ? "user-round-cog" : ((level_key === "level_golden") ? "gem" : "award"))).replaceAll("_", "-")}/>
</RadixThemesBadge>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "start", ["width"] : "100%" })} direction={"column"} justify={"between"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"row"} justify={"between"} gap={"3"}>

<RadixThemesText as={"p"} css={({ ["color"] : "var(--gray-11)" })} size={"3"} weight={"medium"}>

{level_key.replaceAll("level_", "\u0633\u0637\u062d ")}
</RadixThemesText>
<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "end" })} direction={"row"} gap={"2"}>

<RadixThemesHeading size={"7"} weight={"bold"}>

{((JSON.stringify((isTrue(reflex___state____state__customer_data___backend___backend____state.user_counts_by_level_var[level_key]) ? reflex___state____state__customer_data___backend___backend____state.user_counts_by_level_var[level_key] : 0)))+" \u06a9\u0627\u0631\u0628\u0631")}
</RadixThemesHeading>
<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesCard>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
))}</>
</RadixThemesGrid>
  )
}

export function Button_709d45c756253a4cbbfea75917a376ee () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_b139ef4aa1672e906adee41edbb5678b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.first_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton disabled={(reflex___state____state__customer_data___backend___backend____state.current_page_number <= 1)} onClick={on_click_b139ef4aa1672e906adee41edbb5678b} size={"2"} variant={"outline"}>

<LucideChevronsLeft css={({ ["color"] : "var(--current-color)" })}/>
{"\u0627\u0648\u0644\u06cc\u0646"}
</RadixThemesButton>
  )
}

export function Select__root_555cef5f68bf59c26918d6710fff7ba0 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_dd4bff3eb042e1b3d4217b5fcfff2529 = useCallback(((_ev_0) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.sort_values", ({ ["sort_by"] : _ev_0 }), ({  })))], [_ev_0], ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesSelect.Root defaultValue={reflex___state____state__customer_data___backend___backend____state.sort_value} name={"sort_selector"} onValueChange={on_change_dd4bff3eb042e1b3d4217b5fcfff2529} size={"3"}>

<RadixThemesSelect.Trigger placeholder={"\u0645\u0631\u062a\u0628\u200c\u0633\u0627\u0632\u06cc \u0628\u0631 \u0627\u0633\u0627\u0633..."}/>
<RadixThemesSelect.Content>

<RadixThemesSelect.Item value={"created_at_ts"}>

{"\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"username"}>

{"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"national_id"}>

{"\u06a9\u062f \u0645\u0644\u06cc"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"raw_chat_state"}>

{"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"level"}>

{"\u0633\u0637\u062d"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"channel_count"}>

{"\u062a\u0639\u062f\u0627\u062f \u06a9\u0627\u0646\u0627\u0644"}
</RadixThemesSelect.Item>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
  )
}

export function Button_644bb913e121145eb52ab989a69f0443 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_51cff74557c24a3df454f28892d1cb8a = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.last_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton disabled={(reflex___state____state__customer_data___backend___backend____state.current_page_number >= reflex___state____state__customer_data___backend___backend____state.total_pages)} onClick={on_click_51cff74557c24a3df454f28892d1cb8a} size={"2"} variant={"outline"}>

{"\u0622\u062e\u0631\u06cc\u0646"}
<LucideChevronsRight css={({ ["color"] : "var(--current-color)" })}/>
</RadixThemesButton>
  )
}

export function Fragment_c457ec6dea0c67c13e40721053bf6b76 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <Fragment>

{reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (
  <Fragment>

<RadixThemesButton color={"blue"} css={({ ["marginRight"] : "1em" })} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.copy_invite_link", ({  }), ({  })))], args, ({  }))))} size={"2"} variant={"soft"}>

<LucideLink css={({ ["marginRight"] : "0.25em", ["color"] : "var(--current-color)" })} size={16}/>
{"\u062f\u0631\u06cc\u0627\u0641\u062a \u0644\u06cc\u0646\u06a9 \u062f\u0639\u0648\u062a"}
</RadixThemesButton>
</Fragment>
) : (
  <Fragment>

<RadixThemesText as={"p"}>

{""}
</RadixThemesText>
</Fragment>
)}
</Fragment>
  )
}

export function Text_50c10ecc196653b35ab901d893eb5880 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    <RadixThemesText as={"p"} size={"3"}>

{"\u0635\u0641\u062d\u0647 "}
{(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.current_page_number))}
{" \u0627\u0632 "}
{(JSON.stringify(reflex___state____state__customer_data___backend___backend____state.total_pages))}
</RadixThemesText>
  )
}

export function Fragment_ea9b5a5bdd407a583f7d3e04c058741a () {
  
  const { resolvedColorMode } = useContext(ColorModeContext)





  
  return (
    <Fragment>

{(resolvedColorMode === "light") ? (
  <Fragment>

<LucideSun css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideMoon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
  )
}

export function Table__body_6d19c77c8e08d1abe1d2880baccc643d () {
  
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
    <RadixThemesTable.Body>

<>{ reflex___state____state__customer_data___backend___backend____state.paginated_users.map((user, index_e844ff1d989b039c) => (
  <RadixThemesTable.Row align={"center"} css={({ ["&:hover"] : ({ ["background"] : "var(--gray-3)" }) })} key={index_e844ff1d989b039c}>

<RadixThemesTable.Cell>

{(isTrue(user["username"]) ? user["username"] : "-")}
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

{(isTrue(user["national_id"]) ? user["national_id"] : "-")}
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

{(isTrue(user["chat_state_fa"]) ? user["chat_state_fa"] : (isTrue(user["raw_chat_state"]) ? user["raw_chat_state"] : "-"))}
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

{((isNotNullOrUndefined((isTrue(user["level"]) ? user["level"] : null)) && !(((isTrue(user["level"]) ? user["level"] : null) === ""))) ? (((isTrue(user["level"]) ? user["level"] : null) === "_NO_LEVEL_") ? "-" : (isTrue(user["level"]) ? user["level"] : null).replaceAll("level_", "")) : "-")}
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

{(isTrue(user["created_at_str"]) ? user["created_at_str"] : "-")}
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

<Fragment>

{((isTrue(user["channel_count"]) ? user["channel_count"] : 0) > 0) ? (
  <Fragment>

<RadixThemesBadge color={"grass"} radius={"full"} size={"2"} variant={"soft"}>

<LucideUsers css={({ ["color"] : "var(--current-color)" })} size={16}/>
{(("\u0639\u0636\u0648 \u062f\u0631 "+(JSON.stringify((isTrue(user["channel_count"]) ? user["channel_count"] : 0))))+" \u06a9\u0627\u0646\u0627\u0644")}
</RadixThemesBadge>
</Fragment>
) : (
  <Fragment>

<RadixThemesBadge color={"tomato"} radius={"full"} size={"2"} variant={"soft"}>

<LucideUserX css={({ ["color"] : "var(--current-color)" })} size={16}/>
{"\u0639\u0636\u0648 \u0646\u06cc\u0633\u062a"}
</RadixThemesBadge>
</Fragment>
)}
</Fragment>
</RadixThemesTable.Cell>
<RadixThemesTable.Cell>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<RadixThemesDialog.Root>

<RadixThemesDialog.Trigger>

<RadixThemesFlex>

<RadixThemesButton color={"blue"} disabled={((isTrue(user["_id_str"]) ? user["_id_str"] : "") === "")} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.set_current_user_for_edit", ({ ["object_id_str"] : (isTrue(user["_id_str"]) ? user["_id_str"] : "") }), ({  })))], args, ({  }))))} size={"2"} variant={"solid"}>

<LucideSquarePen css={({ ["color"] : "var(--current-color)" })} size={22}/>
<RadixThemesText as={"p"} size={"3"}>

{"\u0648\u06cc\u0631\u0627\u06cc\u0634"}
</RadixThemesText>
</RadixThemesButton>
</RadixThemesFlex>
</RadixThemesDialog.Trigger>
<RadixThemesDialog.Content css={({ ["maxWidth"] : "450px", ["padding"] : "1.5em", ["border"] : "2px solid var(--accent-7)", ["borderRadius"] : "25px" })}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["height"] : "100%", ["marginBottom"] : "1.5em", ["alignItems"] : "center", ["width"] : "100%" })} direction={"row"} gap={"4"}>

<RadixThemesBadge color={"grass"} css={({ ["padding"] : "0.65rem" })} radius={"full"}>

<LucideSquarePen css={({ ["color"] : "var(--current-color)" })} size={34}/>
</RadixThemesBadge>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["height"] : "100%", ["alignItems"] : "start" })} direction={"column"} gap={"1"}>

<RadixThemesDialog.Title css={({ ["weight"] : "bold", ["margin"] : "0" })}>

{"\u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesDialog.Title>
<RadixThemesDialog.Description>

{"\u0627\u0637\u0644\u0627\u0639\u0627\u062a \u06a9\u0627\u0631\u0628\u0631 \u0631\u0627 \u0648\u06cc\u0631\u0627\u06cc\u0634 \u06a9\u0646\u06cc\u062f"}
</RadixThemesDialog.Description>
</RadixThemesFlex>
</RadixThemesFlex>
<RadixThemesFlex css={({ ["width"] : "100%" })} direction={"column"} gap={"4"}>

<Fragment>

{isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (
  <Fragment>

<RadixFormRoot className={"Root "} css={({ ["width"] : "100%" })} onSubmit={handleSubmit_4a3101b7e8deb877c8352cf18ab695b2}>

<RadixThemesFlex direction={"column"} gap={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["alignItems"] : "start", ["width"] : "100%", ["marginBottom"] : "0.75em" })} direction={"column"} gap={"1"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<LucideFingerprint css={({ ["color"] : "var(--current-color)" })} size={16}/>
<RadixThemesText as={"p"} weight={"medium"}>

{"\u0634\u0646\u0627\u0633\u0647 \u062f\u0627\u062e\u0644\u06cc (\u0641\u0642\u0637 \u062e\u0648\u0627\u0646\u062f\u0646\u06cc)"}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesTextField.Root css={({ ["width"] : "100%" })} disabled={true} value={(isNotNullOrUndefined((isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "") : "")) ? (isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["_id_str"] : "") : "") : "")}/>
</RadixThemesFlex>
<RadixFormField className={"Field "} css={({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%" })} name={"username"}>

<RadixThemesFlex direction={"column"} gap={"1"}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideUser css={({ ["strokeWidth"] : 1.5, ["color"] : "var(--current-color)" })} size={16}/>
<RadixFormLabel className={"Label "} css={({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })}>

{"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"}
</RadixFormLabel>
</RadixThemesFlex>
<RadixFormControl asChild={true} className={"Control "}>

<RadixThemesTextField.Root defaultValue={(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["username"] : "") : "")} name={"username"} placeholder={"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"} required={true} type={"text"}/>
</RadixFormControl>
</RadixThemesFlex>
</RadixFormField>
<RadixFormField className={"Field "} css={({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%" })} name={"national_id"}>

<RadixThemesFlex direction={"column"} gap={"1"}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideCreditCard css={({ ["strokeWidth"] : 1.5, ["color"] : "var(--current-color)" })} size={16}/>
<RadixFormLabel className={"Label "} css={({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })}>

{"\u06a9\u062f \u0645\u0644\u06cc"}
</RadixFormLabel>
</RadixThemesFlex>
<RadixFormControl asChild={true} className={"Control "}>

<RadixThemesTextField.Root defaultValue={(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["national_id"] : "") : "")} name={"national_id"} placeholder={"\u06a9\u062f \u0645\u0644\u06cc (\u0627\u062e\u062a\u06cc\u0627\u0631\u06cc)"} required={false} type={"text"}/>
</RadixFormControl>
</RadixThemesFlex>
</RadixFormField>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"1"}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideUserCog css={({ ["strokeWidth"] : 1.5, ["color"] : "var(--current-color)" })} size={16}/>
<RadixThemesText as={"p"}>

{"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesSelect.Root css={({ ["width"] : "100%" })} defaultValue={(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["raw_chat_state"] : "HasAccess") : "HasAccess")} name={"chat_state"} size={"3"}>

<RadixThemesSelect.Trigger placeholder={"\u0627\u0646\u062a\u062e\u0627\u0628 \u0648\u0636\u0639\u06cc\u062a..."}/>
<RadixThemesSelect.Content>

<RadixThemesSelect.Item value={"HasAccess"}>

{"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0627\u0631\u062f"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"HasManualAccess"}>

{"\u062f\u0633\u062a\u0631\u0633\u06cc \u062f\u0633\u062a\u06cc \u062f\u0627\u0631\u062f"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"INITED"}>

{"\u06a9\u0627\u0631\u0628\u0631 \u062c\u062f\u06cc\u062f"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"BLOCKED"}>

{"\u0645\u0633\u062f\u0648\u062f"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"WaitForNationalId"}>

{"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u062f\u0645\u0644\u06cc"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"WaitForOTP"}>

{"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u062f"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"WaitForCaptcha"}>

{"\u062f\u0631 \u0627\u0646\u062a\u0638\u0627\u0631 \u06a9\u067e\u0686\u0627"}
</RadixThemesSelect.Item>
<RadixThemesSelect.Item value={"LoggedIn"}>

{"\u0644\u0627\u06af\u06cc\u0646 \u0634\u062f\u0647"}
</RadixThemesSelect.Item>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%" })} direction={"column"} gap={"1"}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideBarChart2 css={({ ["strokeWidth"] : 1.5, ["color"] : "var(--current-color)" })} size={16}/>
<RadixThemesText as={"p"}>

{"\u0633\u0637\u062d \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesText>
</RadixThemesFlex>
<RadixThemesSelect.Root css={({ ["width"] : "100%" })} defaultValue={(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit) ? (isTrue(reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["level"]) ? reflex___state____state__customer_data___backend___backend____state.current_user_for_edit?.["level"] : "_NO_LEVEL_") : "_NO_LEVEL_")} name={"level"} size={"3"}>

<RadixThemesSelect.Trigger placeholder={"\u0627\u0646\u062a\u062e\u0627\u0628 \u0633\u0637\u062d..."}/>
<RadixThemesSelect.Content>

<>{ reflex___state____state__customer_data___backend___auth_state____auth_state.level_options_for_dropdown.map((opt, index_8af012735d5bd5ee) => (
  <RadixThemesSelect.Item key={index_8af012735d5bd5ee} value={opt.at(1)}>

{opt.at(0)}
</RadixThemesSelect.Item>
))}</>
</RadixThemesSelect.Content>
</RadixThemesSelect.Root>
</RadixThemesFlex>
</RadixThemesFlex>
<RadixThemesFlex css={({ ["paddingTop"] : "2em", ["mt"] : "4" })} justify={"end"} gap={"3"}>

<RadixThemesDialog.Close>

<RadixThemesFlex>

<RadixThemesButton color={"gray"} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.clear_current_user_for_edit", ({  }), ({  })))], args, ({  }))))} variant={"soft"}>

{"\u0644\u063a\u0648"}
</RadixThemesButton>
</RadixThemesFlex>
</RadixThemesDialog.Close>
<RadixFormSubmit asChild={true} className={"Submit "}>

<RadixThemesDialog.Close>

<RadixThemesButton>

{"\u0628\u0647\u200c\u0631\u0648\u0632\u0631\u0633\u0627\u0646\u06cc \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesButton>
</RadixThemesDialog.Close>
</RadixFormSubmit>
</RadixThemesFlex>
</RadixFormRoot>
</Fragment>
) : (
  <Fragment>

<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["height"] : "200px" })}>

<RadixThemesText as={"p"}>

{"\u06a9\u0627\u0631\u0628\u0631\u06cc \u0628\u0631\u0627\u06cc \u0648\u06cc\u0631\u0627\u06cc\u0634 \u0627\u0646\u062a\u062e\u0627\u0628 \u0646\u0634\u062f\u0647 \u06cc\u0627 \u062f\u0631 \u062d\u0627\u0644 \u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc \u0627\u0633\u062a..."}
</RadixThemesText>
</RadixThemesFlex>
</Fragment>
)}
</Fragment>
</RadixThemesFlex>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
<RadixThemesIconButton color={"red"} css={({ ["padding"] : "6px" })} disabled={((isTrue(user["_id_str"]) ? user["_id_str"] : "") === "")} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.delete_customer", ({ ["object_id_str"] : (isTrue(user["_id_str"]) ? user["_id_str"] : "") }), ({  })))], args, ({  }))))} size={"2"} variant={"solid"}>

<LucideTrash2 css={({ ["color"] : "var(--current-color)" })} size={24}/>
</RadixThemesIconButton>
</RadixThemesFlex>
</RadixThemesTable.Cell>
</RadixThemesTable.Row>
))}</>
</RadixThemesTable.Body>
  )
}

export function Iconbutton_aeab80663c2143cee1395db6e50f33d4 () {
  
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])



  
  return (
    <RadixThemesIconButton css={({ ["padding"] : "6px", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) })} onClick={on_click_9922dd3e837b9e087c86a2522c2c93f8} size={"2"}>

<Fragment_ea9b5a5bdd407a583f7d3e04c058741a/>
</RadixThemesIconButton>
  )
}

export function Button_7bced3e188673e3b65da4da47d8dfdd2 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_e286d0bd833f8c44452e8d142cc033ab = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.prev_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton disabled={(reflex___state____state__customer_data___backend___backend____state.current_page_number <= 1)} onClick={on_click_e286d0bd833f8c44452e8d142cc033ab} size={"2"} variant={"outline"}>

<LucideChevronLeft css={({ ["color"] : "var(--current-color)" })}/>
{"\u0642\u0628\u0644\u06cc"}
</RadixThemesButton>
  )
}

export function Fragment_03a58b7c5f99b31d4a012c3c823ed7a8 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <Fragment>

{reflex___state____state__customer_data___backend___backend____state.sort_reverse ? (
  <Fragment>

<LucideArrowDownZA css={({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer", ["color"] : "var(--current-color)" })} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  }))))} size={28}/>
</Fragment>
) : (
  <Fragment>

<LucideArrowDownAZ css={({ ["strokeWidth"] : 1.5, ["cursor"] : "pointer", ["color"] : "var(--current-color)" })} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.toggle_sort", ({  }), ({  })))], args, ({  }))))} size={28}/>
</Fragment>
)}
</Fragment>
  )
}

export function Button_f40d28b6e68ed214ea836751ea972db0 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_4fbf774ab2917adff5ed90557f633c02 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.next_page_handler", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton disabled={(reflex___state____state__customer_data___backend___backend____state.current_page_number >= reflex___state____state__customer_data___backend___backend____state.total_pages)} onClick={on_click_4fbf774ab2917adff5ed90557f633c02} size={"2"} variant={"outline"}>

{"\u0628\u0639\u062f\u06cc"}
<LucideChevronRight css={({ ["color"] : "var(--current-color)" })}/>
</RadixThemesButton>
  )
}

export function Debounceinput_81952d11a48c3150406c93fb8cf3b8f7 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_6c5ff3d4049341dd3eb403ab81e47aa8 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.customer_data___backend___backend____state.filter_values", ({ ["search_term"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    <DebounceInput css={({ ["maxWidth"] : "225px", ["width"] : "100%" })} debounceTimeout={300} element={RadixThemesTextField.Root} onChange={on_change_6c5ff3d4049341dd3eb403ab81e47aa8} placeholder={"\u062c\u0633\u062a\u062c\u0648\u06cc \u06a9\u0627\u0631\u0628\u0631\u0627\u0646..."} size={"3"} value={(isNotNullOrUndefined(reflex___state____state__customer_data___backend___backend____state.search_value) ? reflex___state____state__customer_data___backend___backend____state.search_value : "")} variant={"surface"}>

<RadixThemesTextField.Slot>

<LucideSearch css={({ ["color"] : "var(--current-color)" })}/>
</RadixThemesTextField.Slot>
</DebounceInput>
  )
}

export function Heading_f64f44e8d1ab5843f383890be6ee33a6 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    <RadixThemesHeading size={"7"} weight={"bold"}>

{((JSON.stringify(reflex___state____state__customer_data___backend___backend____state.total_users_for_current_referral))+" \u06a9\u0627\u0631\u0628\u0631")}
</RadixThemesHeading>
  )
}

export function Heading_c0325dca407252a4b40a0804e3d1a140 () {
  
  const reflex___state____state__customer_data___backend___backend____state = useContext(StateContexts.reflex___state____state__customer_data___backend___backend____state)





  
  return (
    <RadixThemesHeading size={"7"} weight={"bold"}>

{((JSON.stringify(reflex___state____state__customer_data___backend___backend____state.users_in_channels_count_var))+" \u0646\u0641\u0631")}
</RadixThemesHeading>
  )
}

export function Fragment_696891d5337ed5a6f781dd29bdc07081 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);





  
  return (
    <Fragment>

{reflex___state____state__customer_data___backend___auth_state____auth_state.is_logged_in ? (
  <Fragment>

<RadixThemesButton color={"red"} onClick={((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.handle_logout", ({  }), ({  })))], args, ({  }))))} size={"2"} variant={"soft"}>

<LucideLogOut css={({ ["color"] : "var(--current-color)" })} size={18}/>
{"\u062e\u0631\u0648\u062c"}
</RadixThemesButton>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<RadixThemesFlex align={"start"} className={"rx-Stack"} css={({ ["width"] : "100%", ["@media screen and (min-width: 0)"] : ({ ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em" }), ["@media screen and (min-width: 30em)"] : ({ ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em" }), ["@media screen and (min-width: 48em)"] : ({ ["paddingInlineStart"] : "3em", ["paddingInlineEnd"] : "3em" }), ["paddingBottom"] : "2em" })} direction={"column"} gap={"6"}>

<RadixThemesFlex align={"center"} css={({ ["@media screen and (min-width: 0)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 30em)"] : ({ ["flexDirection"] : "column" }), ["@media screen and (min-width: 48em)"] : ({ ["flexDirection"] : "row" }), ["width"] : "100%", ["top"] : "0px", ["paddingTop"] : "1em", ["paddingBottom"] : "1em", ["paddingInlineStart"] : "1.5em", ["paddingInlineEnd"] : "1.5em", ["borderBottom"] : "1px solid var(--gray-a5)", ["background"] : "var(--gray-1)" })} gap={"2"}>

<RadixThemesBadge color={"green"} css={({ ["align"] : "center", ["padding"] : "0.65rem" })} radius={"large"} variant={"surface"}>

<LucideTable2 css={({ ["color"] : "var(--current-color)" })} size={28}/>
<RadixThemesHeading css={({ ["direction"] : "rtl" })} size={"6"}>

{"\u067e\u0646\u0644 \u06a9\u0627\u0631\u0628\u0631\u0627\u0646"}
</RadixThemesHeading>
</RadixThemesBadge>
<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Fragment_c457ec6dea0c67c13e40721053bf6b76/>
<Iconbutton_aeab80663c2143cee1395db6e50f33d4/>
<Fragment_696891d5337ed5a6f781dd29bdc07081/>
</RadixThemesFlex>
</RadixThemesFlex>
<Grid_81454f8cc7102014a5f755589cbe32ec/>
<RadixThemesBox css={({ ["width"] : "100%" })}>

<Fragment>

<RadixThemesFlex align={"center"} css={({ ["width"] : "100%", ["paddingBottom"] : "1em" })} justify={"end"} gap={"3"} wrap={"wrap"}>

<RadixThemesFlex css={({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })}/>
<Fragment_03a58b7c5f99b31d4a012c3c823ed7a8/>
<Select__root_555cef5f68bf59c26918d6710fff7ba0/>
<Debounceinput_81952d11a48c3150406c93fb8cf3b8f7/>
</RadixThemesFlex>
<RadixThemesTable.Root css={({ ["width"] : "100%" })} size={"3"} variant={"surface"}>

<RadixThemesTable.Header>

<RadixThemesTable.Row>

<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideUser css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideCreditCard css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u06a9\u062f \u0645\u0644\u06cc"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideUserCog css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u0648\u0636\u0639\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideBarChartHorizontalBig css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u0633\u0637\u062d"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideCalendar css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideUsers css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u0648\u0636\u0639\u06cc\u062a \u0639\u0636\u0648\u06cc\u062a"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
<RadixThemesTable.ColumnHeaderCell>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"2"}>

<LucideCog css={({ ["color"] : "var(--current-color)" })} size={18}/>
<RadixThemesText as={"p"}>

{"\u0639\u0645\u0644\u06cc\u0627\u062a"}
</RadixThemesText>
</RadixThemesFlex>
</RadixThemesTable.ColumnHeaderCell>
</RadixThemesTable.Row>
</RadixThemesTable.Header>
<Table__body_6d19c77c8e08d1abe1d2880baccc643d/>
</RadixThemesTable.Root>
<RadixThemesFlex align={"center"} className={"rx-Stack"} css={({ ["width"] : "100%", ["paddingTop"] : "1em", ["paddingBottom"] : "1em" })} direction={"row"} justify={"center"} gap={"3"}>

<Button_709d45c756253a4cbbfea75917a376ee/>
<Button_7bced3e188673e3b65da4da47d8dfdd2/>
<Text_50c10ecc196653b35ab901d893eb5880/>
<Button_f40d28b6e68ed214ea836751ea972db0/>
<Button_644bb913e121145eb52ab989a69f0443/>
</RadixThemesFlex>
</Fragment>
</RadixThemesBox>
</RadixThemesFlex>
<NextHead>

<title>

{"\u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u0627\u0631\u0628\u0631\u0627\u0646"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
