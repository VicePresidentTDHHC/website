import { defineConfig } from "vite";

export default defineConfig({
  root: "www",
  publicDir: false,
  server: {
    host: true,
    port: 5173,
  },
});
