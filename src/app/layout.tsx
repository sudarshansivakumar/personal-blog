import type { Metadata } from "next";
import { Geist, Geist_Mono, EB_Garamond, Playfair_Display } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Elegant serif for body text (like New Yorker's Caslon)
const ebGaramond = EB_Garamond({
  variable: "--font-eb-garamond",
  subsets: ["latin"],
  display: "swap",
});

// More distinctive serif for headings
const playfairDisplay = Playfair_Display({
  variable: "--font-playfair",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Hello world",
  description: "Welcome to the repository of my intrusive thoughts",
  icons: [
    { rel: 'icon', url: '/icon.png' },
    { rel: 'apple-touch-icon', url: '/icon.png' }
  ]
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${ebGaramond.variable} ${playfairDisplay.variable} antialiased`}
      >
        <div className="min-h-screen">
          <Header />
          {children}
        </div>
      </body>
    </html>
  );
}
