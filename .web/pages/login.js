/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Button as RadixThemesButton, Callout as RadixThemesCallout, Flex as RadixThemesFlex, Heading as RadixThemesHeading, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { Field as RadixFormField, Label as RadixFormLabel, Root as RadixFormRoot } from "@radix-ui/react-form"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getRefValue, getRefValues, isNotNullOrUndefined, isTrue } from "$/utils/state"
import { KeyRound as LucideKeyRound, ShieldAlert as LucideShieldAlert, User as LucideUser } from "lucide-react"
import { DebounceInput } from "react-debounce-input"
import NextHead from "next/head"
import { jsx } from "@emotion/react"



export function Debounceinput_df0ac1161342897bd6b435f6238a857f () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_a09f472fadc20a84f1163a0597c1e472 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.set_entered_password", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(DebounceInput,{css:({ ["width"] : "300px" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_a09f472fadc20a84f1163a0597c1e472,placeholder:"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631...",size:"3",type:"password",value:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___auth_state____auth_state.entered_password) ? reflex___state____state__customer_data___backend___auth_state____auth_state.entered_password : "")},)

  )
}

export function Root_a9274d65806677317db0425d87a24a1f () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  
    const handleSubmit_e33a05fb7e4e69de318f127979cd6fdc = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.handle_login", ({  }), ({  })))], args, ({  }))))(ev));

        if (false) {
            $form.reset()
        }
    })
    




  
  return (
    jsx(
RadixFormRoot,
{className:"Root ",css:({ ["width"] : "auto" }),onSubmit:handleSubmit_e33a05fb7e4e69de318f127979cd6fdc},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"column",gap:"4"},
jsx(
RadixFormField,
{className:"Field ",css:({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%", ["alignItems"] : "center" }),name:"username_field"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideUser,{size:18},)
,jsx(
RadixFormLabel,
{className:"Label ",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })},
"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc \u0627\u062f\u0645\u06cc\u0646"
,),),jsx(Debounceinput_328554e00761a2fb76589cfa7468ad68,{},)
,),jsx(
RadixFormField,
{className:"Field ",css:({ ["display"] : "grid", ["marginBottom"] : "10px", ["width"] : "100%", ["alignItems"] : "center" }),name:"password_field"},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["alignItems"] : "center" }),direction:"row",gap:"3"},
jsx(LucideKeyRound,{size:18},)
,jsx(
RadixFormLabel,
{className:"Label ",css:({ ["fontSize"] : "15px", ["fontWeight"] : "500", ["lineHeight"] : "35px" })},
"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631"
,),),jsx(Debounceinput_df0ac1161342897bd6b435f6238a857f,{},)
,),jsx(Fragment_617c8c04aa69b7df4cfa5dd69d97e510,{},)
,jsx(
RadixThemesButton,
{color:"grass",css:({ ["width"] : "300px", ["marginTop"] : "1em" }),size:"3",type:"submit"},
"\u0648\u0631\u0648\u062f"
,),),)
  )
}

export function Debounceinput_328554e00761a2fb76589cfa7468ad68 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_595807808c1193bd141fdc6b1ba5f849 = useCallback(((_e) => (addEvents([(Event("reflex___state____state.customer_data___backend___auth_state____auth_state.set_entered_username", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    jsx(DebounceInput,{css:({ ["width"] : "300px" }),debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_595807808c1193bd141fdc6b1ba5f849,placeholder:"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc...",size:"3",value:(isNotNullOrUndefined(reflex___state____state__customer_data___backend___auth_state____auth_state.entered_username) ? reflex___state____state__customer_data___backend___auth_state____auth_state.entered_username : "")},)

  )
}

export function Fragment_617c8c04aa69b7df4cfa5dd69d97e510 () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
Fragment,
{},
(!((reflex___state____state__customer_data___backend___auth_state____auth_state.error_message === "")) ? (jsx(
Fragment,
{},
jsx(
RadixThemesCallout.Root,
{color:"red",css:({ ["marginTop"] : "1em", ["width"] : "300px" }),variant:"soft"},
jsx(
RadixThemesCallout.Icon,
{},
jsx(LucideShieldAlert,{},)
,),jsx(Callout__text_d2afa9ce678df8a465af73d67d8a0c5c,{},)
,),)) : (jsx(Fragment,{},)
)),)
  )
}

export function Callout__text_d2afa9ce678df8a465af73d67d8a0c5c () {
  
  const reflex___state____state__customer_data___backend___auth_state____auth_state = useContext(StateContexts.reflex___state____state__customer_data___backend___auth_state____auth_state)





  
  return (
    jsx(
RadixThemesCallout.Text,
{},
reflex___state____state__customer_data___backend___auth_state____auth_state.error_message
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
{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["height"] : "100vh", ["width"] : "100%" })},
jsx(
RadixThemesFlex,
{align:"start",className:"rx-Stack",css:({ ["padding"] : "2em", ["borderRadius"] : "md", ["boxShadow"] : "lg", ["background"] : "var(--gray-2)", ["alignItems"] : "center" }),direction:"column",gap:"3"},
jsx(
RadixThemesHeading,
{css:({ ["textAlign"] : "center", ["marginBottom"] : "1em" }),size:"7"},
"\u0648\u0631\u0648\u062f \u0628\u0647 \u067e\u0646\u0644 \u0627\u062f\u0645\u06cc\u0646"
,),jsx(Root_a9274d65806677317db0425d87a24a1f,{},)
,),),jsx(
NextHead,
{},
jsx(
"title",
{},
"\u0648\u0631\u0648\u062f \u0628\u0647 \u067e\u0646\u0644"
,),jsx("meta",{content:"favicon.ico",property:"og:image"},)
,),)
  )
}
