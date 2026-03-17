"use client";

/**
 * OfferBuilder — responsive offer line editor
 *
 * Desktop  : full table-like layout with drag-to-reorder
 * Mobile   : stacked card list, each card collapsible
 *
 * This component is purely a controlled UI — the parent page owns the state
 * and submission via React Hook Form or similar.
 */

import { useCallback, useId } from "react";
import { Plus, FileText, AlignLeft, Calculator } from "lucide-react";
import { cn } from "@/lib/utils";
import { OfferLineCard, OfferLineData } from "./offer-line-card";

// ─── Props ────────────────────────────────────────────────────────────────────

interface OfferBuilderProps {
  lines: OfferLineData[];
  onChange: (lines: OfferLineData[]) => void;
  /** Available currencies for the price input selector */
  currencies?: string[];
  /** EGP exchange rates — used to compute line_total_egp client-side */
  fxRates?: Record<string, number>; // e.g. { USD: 48.5, EUR: 52.1 }
  className?: string;
}

// ─── Totals summary ──────────────────────────────────────────────────────────

function TotalsSummary({
  lines,
  fxRates,
}: {
  lines: OfferLineData[];
  fxRates: Record<string, number>;
}) {
  const productLines = lines.filter((l) => l.line_type === "product");

  const subtotalEgp = productLines.reduce((sum, l) => {
    if (l.line_total_egp != null) return sum + l.line_total_egp;
    // Compute on the fly if not pre-computed
    const qty = l.quantity ?? 0;
    const price = l.unit_price_foreign ?? 0;
    const fx = fxRates[l.currency ?? "EGP"] ?? 1;
    const disc = 1 - (l.discount_pct ?? 0) / 100;
    return sum + qty * price * fx * disc;
  }, 0);

  const vatAmt = subtotalEgp * 0.14;
  const total = subtotalEgp + vatAmt;

  const fmt = (n: number) =>
    n.toLocaleString("en-EG", { minimumFractionDigits: 2 });

  return (
    <div className="rounded-xl border border-border bg-card p-4 space-y-2">
      <div className="flex justify-between text-sm">
        <span className="text-muted-foreground">Subtotal</span>
        <span className="font-medium">EGP {fmt(subtotalEgp)}</span>
      </div>
      <div className="flex justify-between text-sm">
        <span className="text-muted-foreground">VAT (14%)</span>
        <span className="font-medium">EGP {fmt(vatAmt)}</span>
      </div>
      <div className="flex justify-between text-sm border-t border-border pt-2">
        <span className="font-semibold text-foreground">Total</span>
        <span className="font-bold text-gamma-blue text-base">
          EGP {fmt(total)}
        </span>
      </div>
    </div>
  );
}

// ─── Component ───────────────────────────────────────────────────────────────

export function OfferBuilder({
  lines,
  onChange,
  currencies = ["USD", "EUR", "EGP"],
  fxRates = {},
  className,
}: OfferBuilderProps) {
  const uid = useId();

  const makeId = () => `${uid}-${Date.now()}-${Math.random().toString(36).slice(2)}`;

  // Add a new product line
  const addProductLine = useCallback(() => {
    const newLine: OfferLineData = {
      id: makeId(),
      sort_order: lines.length,
      line_type: "product",
      quantity: 1,
      unit_of_measure: "pcs",
      currency: "USD",
      discount_pct: 0,
    };
    onChange([...lines, newLine]);
  }, [lines, onChange]);

  // Add a section header line
  const addSectionHeader = useCallback(() => {
    onChange([
      ...lines,
      {
        id: makeId(),
        sort_order: lines.length,
        line_type: "section_header",
        description: "",
      },
    ]);
  }, [lines, onChange]);

  // Add a note line
  const addNote = useCallback(() => {
    onChange([
      ...lines,
      {
        id: makeId(),
        sort_order: lines.length,
        line_type: "note",
        notes: "",
      },
    ]);
  }, [lines, onChange]);

  // Update a single line by id
  const updateLine = useCallback(
    (id: string, changes: Partial<OfferLineData>) => {
      onChange(
        lines.map((l) => {
          if (l.id !== id) return l;
          const updated = { ...l, ...changes };

          // Recompute line total on price/qty/discount change
          if (
            "quantity" in changes ||
            "unit_price_foreign" in changes ||
            "currency" in changes ||
            "discount_pct" in changes
          ) {
            const qty = updated.quantity ?? 0;
            const price = updated.unit_price_foreign ?? 0;
            const fx = fxRates[updated.currency ?? "EGP"] ?? 1;
            const disc = 1 - (updated.discount_pct ?? 0) / 100;
            updated.line_total_egp = qty * price * fx * disc;
          }

          return updated;
        })
      );
    },
    [lines, onChange, fxRates]
  );

  // Remove a line by id
  const removeLine = useCallback(
    (id: string) => {
      onChange(lines.filter((l) => l.id !== id));
    },
    [lines, onChange]
  );

  // Move a line up or down (mobile fallback — no DnD lib needed)
  const moveLine = useCallback(
    (id: string, direction: "up" | "down") => {
      const idx = lines.findIndex((l) => l.id === id);
      if (idx < 0) return;
      const newLines = [...lines];
      const swapWith = direction === "up" ? idx - 1 : idx + 1;
      if (swapWith < 0 || swapWith >= newLines.length) return;
      [newLines[idx], newLines[swapWith]] = [newLines[swapWith], newLines[idx]];
      onChange(newLines.map((l, i) => ({ ...l, sort_order: i })));
    },
    [lines, onChange]
  );

  const productLineCount = lines.filter((l) => l.line_type === "product").length;

  return (
    <div className={cn("space-y-3", className)}>
      {/* Column headers — desktop only */}
      <div className="hidden lg:grid grid-cols-[32px_1fr_80px_80px_160px_80px_120px_32px] gap-2 px-3 text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
        <span />
        <span>#  Product</span>
        <span>Qty</span>
        <span>UOM</span>
        <span>Unit Price</span>
        <span>Disc %</span>
        <span className="text-right">Line Total</span>
        <span />
      </div>

      {/* Lines */}
      {lines.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-10 text-center text-muted-foreground border border-dashed border-border rounded-xl">
          <FileText className="h-8 w-8 mb-2 opacity-40" />
          <p className="text-sm">No lines yet.</p>
          <p className="text-xs mt-1">Add a product line to get started.</p>
        </div>
      ) : (
        <div className="space-y-2">
          {lines.map((line, idx) => (
            <OfferLineCard
              key={line.id}
              line={line}
              index={idx}
              onUpdate={updateLine}
              onRemove={removeLine}
              currencies={currencies}
            />
          ))}
        </div>
      )}

      {/* Add buttons */}
      <div className="flex flex-wrap gap-2 pt-1">
        <button
          type="button"
          onClick={addProductLine}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-dashed border-gamma-blue/50 text-gamma-blue text-sm font-medium hover:bg-gamma-blue/5 transition-colors"
        >
          <Plus className="h-4 w-4" />
          Add Product
        </button>
        <button
          type="button"
          onClick={addSectionHeader}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-dashed border-gamma-gold/50 text-gamma-gold text-sm font-medium hover:bg-gamma-gold/5 transition-colors"
        >
          <AlignLeft className="h-4 w-4" />
          Section Header
        </button>
        <button
          type="button"
          onClick={addNote}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-dashed border-border text-muted-foreground text-sm font-medium hover:bg-muted transition-colors"
        >
          <FileText className="h-4 w-4" />
          Note
        </button>
      </div>

      {/* Totals */}
      {productLineCount > 0 && (
        <div className="pt-2">
          <div className="flex items-center gap-2 mb-2">
            <Calculator className="h-4 w-4 text-muted-foreground" />
            <span className="text-xs font-medium text-muted-foreground uppercase tracking-wide">
              Totals
            </span>
          </div>
          <TotalsSummary lines={lines} fxRates={fxRates} />
        </div>
      )}
    </div>
  );
}
