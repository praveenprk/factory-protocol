// ESLint for the page's inline <script> (DECISION-003, ENG-STD-004 §6.1).
// index.html is generated from factory-protocol.html (scripts/build_index.py),
// so only the source page is linted.
import js from "@eslint/js";
import html from "eslint-plugin-html";

export default [
  { ignores: ["index.html", "node_modules/", ".venv/"] },
  js.configs.recommended,
  {
    files: ["factory-protocol.html"],
    plugins: { html },
    languageOptions: {
      ecmaVersion: 5,
      sourceType: "script",
      globals: { document: "readonly" },
    },
  },
];
