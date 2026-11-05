import { defineConfig } from "astro/config";

export default defineConfig({
  // Explicit static output: one HTML/CSS/JS/asset tree in dist/, no Node server.
  // Fits the HTL Abgabe and Portato static hosting at schoolportfolio.emilioschwaiger.com.
  output: "static",
  site: "https://schoolportfolio.emilioschwaiger.com",
  trailingSlash: "never",
  build: {
    format: "file",
    inlineStylesheets: "always",
  },
});
