"use client";
import { useState } from "react";
import { Sidebar } from "@/components/navigation/sidebar";
import { BottomNav } from "@/components/navigation/bottom-nav";
import { TopBar } from "@/components/navigation/top-bar";

export function AppShell({ children }: { children: React.ReactNode }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="flex h-screen bg-gray-50 dark:bg-gray-950 overflow-hidden">
      {/* ── Desktop Sidebar ── */}
      <aside className="hidden lg:flex lg:flex-col lg:w-64 lg:fixed lg:inset-y-0 z-30">
        <Sidebar />
      </aside>

      {/* ── Mobile Sidebar Drawer ── */}
      {sidebarOpen && (
        <div className="lg:hidden fixed inset-0 z-40 flex">
          <div
            className="fixed inset-0 bg-black/50"
            onClick={() => setSidebarOpen(false)}
          />
          <aside className="relative w-72 flex flex-col bg-white dark:bg-gray-900 shadow-xl z-50">
            <Sidebar onClose={() => setSidebarOpen(false)} />
          </aside>
        </div>
      )}

      {/* ── Main Content ── */}
      <div className="flex-1 flex flex-col lg:pl-64 min-h-0">
        <TopBar onMenuClick={() => setSidebarOpen(true)} />

        <main className="flex-1 overflow-y-auto pb-20 lg:pb-6 px-4 lg:px-6 pt-4">
          {children}
        </main>
      </div>

      {/* ── Mobile Bottom Navigation ── */}
      <div className="lg:hidden">
        <BottomNav />
      </div>
    </div>
  );
}
