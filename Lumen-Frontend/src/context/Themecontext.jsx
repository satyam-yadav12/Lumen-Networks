//  darkMode: "class", // 👈 IMPORTANT
import { createContext, useEffect, useState } from "react";

export const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");
  const [Imgtag, setImgtag] = useState("hero");

  useEffect(() => {
    // apply Tailwind dark mode class
    if (theme === "dark") {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  useEffect(() => {
    setImgtag(theme === "dark" ? "dark" : "hero");
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme, Imgtag }}>
      {children}
    </ThemeContext.Provider>
  );
}
