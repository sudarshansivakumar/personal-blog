import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          bg: '#0f1012',
          'bg-light': '#232427', 
          text: '#e8e6e3',
          'text-muted': '#a6a4a1',
          accent: '#82a0ff',
          border: '#232427',
        }
      },
      fontFamily: {
        'garamond': ['var(--font-eb-garamond)', 'Garamond', 'Georgia', 'serif'],
        'playfair': ['var(--font-playfair)', 'Playfair Display', 'Georgia', 'serif'],
        'sans': ['var(--font-geist-sans)', 'ui-sans-serif', 'system-ui'],
        'mono': ['var(--font-geist-mono)', 'ui-monospace', 'SFMono-Regular'],
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};

export default config; 