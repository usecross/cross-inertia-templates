import { defineConfig } from "vite";
import inertia from '@inertiajs/vite'

import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react(), inertia()],
});
