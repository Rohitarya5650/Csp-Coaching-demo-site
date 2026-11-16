/** Royal Blue + White + Energetic Orange/Yellow */
module.exports = {
  content: ["./*.html", "./assets/js/*.js"],
  theme: {
    extend: {
      colors: {
        royal: { 50: "#eef3ff", 100: "#dce7ff", 200: "#b9ceff", 400: "#4f7aee", 500: "#2b57d8", 600: "#1f44b8", 700: "#183694", 800: "#122a73", 900: "#0b1c50", 950: "#071238" },
        orange: { DEFAULT: "#ff8a1f", 600: "#e87100", 100: "#ffeedb" },
        sun: { DEFAULT: "#ffc21a", 100: "#fff4d1" },
        ink: "#0b1c50",
      },
      fontFamily: {
        display: ['"Bricolage Grotesque"', '"Mukta"', "system-ui", "sans-serif"],
        body: ['"Mukta"', '"Bricolage Grotesque"', "system-ui", "sans-serif"],
      },
      keyframes: {
        marquee: { from: { transform: "translateX(0)" }, to: { transform: "translateX(-50%)" } },
        floaty: { "0%,100%": { transform: "translateY(0)" }, "50%": { transform: "translateY(-8px)" } },
        fadeup: { from: { opacity: 0, transform: "translateY(14px)" }, to: { opacity: 1, transform: "none" } },
      },
      animation: { marquee: "marquee 40s linear infinite", floaty: "floaty 5s ease-in-out infinite", fadeup: "fadeup .7s ease both" },
      boxShadow: { card: "0 1px 2px rgba(11,28,80,.06), 0 10px 30px rgba(11,28,80,.10)", lift: "0 18px 50px rgba(11,28,80,.20)" },
    },
  },
  plugins: [],
};
