<template>
    <div>
        <hero></hero>
<!--        <basic-elements></basic-elements>-->
<!--        <inputs></inputs>-->
<!--        <custom-controls></custom-controls>-->
<!--        <navigation></navigation>-->
<!--        <javascript-components></javascript-components>-->
<!--        <icons></icons>-->
<!--        <examples></examples>-->
<!--        <download-section></download-section>-->
<!--        <carousel></carousel>-->
    </div>
</template>
<script>
import Hero from "./components/Hero";
import BasicElements from "./components/BasicElements";
import Inputs from "./components/Inputs";
import CustomControls from "./components/CustomControls";
import Navigation from "./components/Navigation";
import JavascriptComponents from "./components/JavascriptComponents";
import Examples from "./components/Examples";

export default {
  name: "components",
  components: {
    Hero,
    BasicElements,
    Inputs,
    CustomControls,
    Navigation,
    JavascriptComponents,
    Examples,
  }
};
</script>
