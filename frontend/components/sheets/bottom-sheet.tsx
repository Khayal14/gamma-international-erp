"use client";
import { useEffect, useRef } from "react";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";

interface BottomSheetProps {
  open: boolean;
  onClose: () => void;
  title?: string;
  children: React.ReactNode;
  /** "full" uses 90vh; "auto" fits content */
  size?: "auto" | "full";
}

export function BottomSheet({ open, onClose, title, children, size = "auto" }: BottomSheetProps) {
  const sheetRef = useRef<HTMLDivElement>(null);

  // Close on Escape
  useEffect(() => {
    const handler = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [onClose]);

  // Lock body scroll when open
  useEffect(() => {
    if (open) document.body.style.overflow = "hidden";
    else document.body.style.overflow = "";
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-end lg:items-center lg:justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Sheet / Dialog */}
      <div
        ref={sheetRef}
        className={cn(
          "relative w-full bg-white dark:bg-gray-900 shadow-2xl",
          // Mobile: slide up from bottom with rounded top corners
          "rounded-t-2xl lg:rounded-2xl",
          // Desktop: standard centered dialog with max width
          "lg:max-w-2xl lg:w-full lg:mx-4",
          // Height
          size === "full"
            ? "max-h-[90vh] lg:max-h-[80vh]"
            : "max-h-[85vh] lg:max-h-[80vh]",
          "flex flex-col"
        )}
      >
        {/* Drag handle (mobile only) */}
        <div className="lg:hidden flex justify-center pt-3 pb-1 shrink-0">
          <div className="w-10 h-1 rounded-full bg-gray-300 dark:bg-gray-700" />
        </div>

        {/* Header */}
        {title && (
          <div className="flex items-center justify-between px-5 py-3 border-b
                          border-gray-200 dark:border-gray-800 shrink-0">
            <h2 className="text-base font-semibold text-gray-900 dark:text-white">
              {title}
            </h2>
            <button
              onClick={onClose}
              className="p-1.5 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 text-gray-500"
            >
              <X size={18} />
            </button>
          </div>
        )}

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto overscroll-contain">
          {children}
        </div>
      </div>
    </div>
  );
}
