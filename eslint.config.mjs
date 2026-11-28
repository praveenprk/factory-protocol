// ESLint for the page's inline <script> (DECISION-003, DECISION-008, ENG-STD-004 §6.1).
import js from "@eslint/js";
import html from "eslint-plugin-html";

export default [
  { ignores: ["node_modules/", ".venv/"] },
  js.configs.recommended,
  {
    files: ["index.html"],
    plugins: { html },
    languageOptions: {
      ecmaVersion: 5,
      sourceType: "script",
      globals: { document: "readonly" },
    },
  },
];
