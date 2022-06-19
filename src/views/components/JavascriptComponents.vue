<template>
    <section class="section section-components">
        <div class="container">
            <progress-section></progress-section>
            <div class="row row-grid justify-content-between">
            </div>
            <h3 class="mt-lg mb-4">
                <span>Alerts</span>
            </h3>
            <typography></typography>
            <!-- Images -->
            <h2 class="mt-lg mb-5">
                <span>Images</span>
            </h2>
            <images></images>
            <h2 class="mt-lg mb-5">
                <span>Javascript Components</span>
            </h2>
            <h3 class="h4 text-success font-weight-bold mb-4">Modals</h3>
            <!-- Modals -->
            <modals></modals>
             Datepicker
            <h3 class="h4 text-success font-weight-bold mt-md mb-4">Datepicker</h3>
            <date-pickers></date-pickers>
            <!-- Tooltips and Popovers -->
            <h3 class="h4 text-success font-weight-bold mt-md mb-4">Tooltips &amp; Popovers</h3>
            <tooltips></tooltips>
        </div>
    </section>
</template>
<script>
// import Tabs from "@/components/Tabs/Tabs.vue";
// import TabPane from "@/components/Tabs/TabPane.vue";
import Modals from "./JavascriptComponents/Modals";
// const Tooltips = () => import("./JavascriptComponents/Tooltips");
// const DatePickers = () => import("./JavascriptComponents/DatePickers");
import Images from "./JavascriptComponents/Images";
// import TabsSection from "./JavascriptComponents/TabsSection";
import ProgressSection from "./JavascriptComponents/ProgressPagination";
// import Typography from "./JavascriptComponents/Typography";

export default {
  components: {
    // DatePickers,
    Images,
    Modals,
    // TabPane,
    // Tabs,
    // TabsSection,
    ProgressSection,
    // Typography,
    // Tooltips
  }
};
</script>
<style>
</style>
