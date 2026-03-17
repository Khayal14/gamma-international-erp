"use client";
import { useState } from "react";

export function LanguageToggle() {
  const [lang, setLang] = useState<"EN" | "AR">("EN");

  const toggle = () => {
    const next = lang === "EN" ? "AR" : "EN";
    setLang(next);
    document.documentElement.lang = next === "AR" ? "ar" : "en";
    document.documentElement.dir  = next === "AR" ? "rtl" : "ltr";
  };

  return (
    <button
      onClick={toggle}
      className="px-2.5 py-1.5 rounded-lg text-xs font-bold
                 hover:bg-gray-100 dark:hover:bg-gray-800
                 text-gray-600 dark:text-gray-300 border border-gray-200 dark:border-gray-700"
    >
      {lang === "EN" ? "عربي" : "EN"}
    </button>
  );
}
