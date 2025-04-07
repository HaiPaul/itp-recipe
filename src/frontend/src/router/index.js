import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProfileView from "../views/ProfileView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import LogoutView from "../views/LogoutView.vue";
import RefreshView from "../views/RefreshView.vue";
import BrowseView from "../views/BrowseView.vue";
import CreateRecipe from "../views/CreateRecipe.vue";
import RecipeDetail from "../views/RecipeDetail.vue";
import MyRecipes from "../views/MyRecipes.vue";
import { useAuthStore } from "../store/auth";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/recipe/:id",
    name: "RecipeDetail",
    component: RecipeDetail,
    props: true,
  },
  {
    path: "/create",
    name: "Create",
    component: CreateRecipe,
  },
  {
    path: "/create",
    name: "Create",
    component: CreateRecipe,
  },
  {
    path: "/myRecipes",
    name: "MyRecipes",
    component: BrowseView,
  },
  {
    path: "/browse",
    name: "Browse",
    component: BrowseView,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: "/logout",
    name: "Logout",
    component: LogoutView,
  },
  {
    path: "/refresh",
    name: "Refresh",
    component: RefreshView,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (auth.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
