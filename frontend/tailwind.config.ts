import type { Config } from "tailwindcss";
const config: Config = {
  darkMode: "class",
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        gamma: {
          blue:  "#1A56C4",
          gold:  "#F5A800",
          dark:  "#1A2E4A",
        },
        category: {
          led:   "#B45309",
          heat:  "#B91C1C",
          solar: "#065F46",
          trade: "#5B21B6",
        },
      },
      fontFamily: {
        sans: ["Inter", "Noto Sans Arabic", "sans-serif"],
      },
    },
  },
  plugins: [],
};
export default config;
