/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./src/**/*.{js,jsx,ts,tsx}",
    ],

    theme: {
        extend: {},
    },
    daisyui: {
        themes: [
            {
                mytheme: {
                    "primary": "#5eead4",
                    "secondary": "#064d60",
                    "accent": "#e2705f",
                    "neutral": "#362a3c",
                    "base-100": "#eeeef1",
                    "info": "#41a2e6",
                    "success": "#40e2b7",
                    "warning": "#a66811",
                    "error": "#be123c",
                },
            },
        ],
    },
    plugins: [require("daisyui")],
}

