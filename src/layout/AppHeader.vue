<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent type="" effect="light" expand>
            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="https://demos.creative-tim.com/vue-argon-design-system/documentation/">
                        <img src="img/brand/3.png">
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>
<!--          <ul class="navbar-nav navbar-nav-hover align-items-lg-center">-->
<!--            <base-dropdown tag="li" class="nav-item">-->
<!--              <a slot="title" href="#" class="nav-link" data-toggle="dropdown" role="button">-->
<!--                <i class="ni ni-collection d-lg-none"></i>-->
<!--                <span class="nav-link-inner&#45;&#45;text text-black-50">Examples</span>-->
<!--              </a>-->
<!--              <router-link to="/landing" class="dropdown-item text-black-50">Landing</router-link>-->
<!--            </base-dropdown>-->
<!--          </ul>-->

        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown
  }
};
</script>
<style>
</style>
