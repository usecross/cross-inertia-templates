import { defineConfig } from "vite";
import inertia from '@inertiajs/vite'

import react from "@vitejs/plugin-react";

export default defineConfig(({ command }) => ({
  // Built assets are served by FastAPI under /static/build. The dev server
  // keeps the root base, where CrossInertia loads /@vite/client and the entry.
  base: command === "build" ? "/static/build/" : "/",
  plugins: [react(), inertia()],
  build: {
    outDir: "static/build",
    manifest: true,
    rolldownOptions: {
      input: "frontend/app.tsx",
    },
  },
}));
