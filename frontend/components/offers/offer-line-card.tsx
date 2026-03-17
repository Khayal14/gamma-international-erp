"use client";

import { Trash2, GripVertical, ChevronDown, ChevronUp } from "lucide-react";
import { useState } from "react";
import { cn } from "@/lib/utils";

export interface OfferLineData {
  id: string;
  sort_order: number;
  line_type: "product" | "section_header" | "note";
  description?: string;
  product_variant_id?: string;
  product_code?: string;
  product_name?: string;
  quantity?: number;
  unit_of_measure?: string;
  unit_price_foreign?: number;
  currency?: string;
  unit_price_egp?: number;
  discount_pct?: number;
  line_total_egp?: number;
  notes?: string;
}

interface OfferLineCardProps {
  line: OfferLineData;
  index: number;
  onUpdate: (id: string, changes: Partial<OfferLineData>) => void;
  onRemove: (id: string) => void;
  currencies: string[];
  /** Drag handle props if using dnd-kit or similar */
  dragHandleProps?: Record<string, unknown>;
  isDragging?: boolean;
}

export function OfferLineCard({
  line,
  index,
  onUpdate,
  onRemove,
  currencies,
  dragHandleProps,
  isDragging = false,
}: OfferLineCardProps) {
  const [expanded, setExpanded] = useState(true);

  if (line.line_type === "section_header") {
    return (
      <div
        className={cn(
          "flex items-center gap-2 px-3 py-2 rounded-lg bg-gamma-gold/10 border border-gamma-gold/30",
          isDragging && "opacity-50 shadow-xl"
        )}
      >
        <div {...(dragHandleProps as object)} className="cursor-grab touch-none">
          <GripVertical className="h-4 w-4 text-muted-foreground" />
        </div>
        <input
          className="flex-1 bg-transparent text-sm font-semibold text-gamma-gold placeholder:text-gamma-gold/50 outline-none"
          placeholder="Section header…"
          value={line.description ?? ""}
          onChange={(e) => onUpdate(line.id, { description: e.target.value })}
        />
        <button
          type="button"
          onClick={() => onRemove(line.id)}
          className="text-muted-foreground hover:text-destructive transition-colors"
        >
          <Trash2 className="h-4 w-4" />
        </button>
      </div>
    );
  }

  if (line.line_type === "note") {
    return (
      <div
        className={cn(
          "flex items-start gap-2 px-3 py-2 rounded-lg bg-muted/40 border border-border",
          isDragging && "opacity-50 shadow-xl"
        )}
      >
        <div {...(dragHandleProps as object)} className="cursor-grab touch-none mt-0.5">
          <GripVertical className="h-4 w-4 text-muted-foreground" />
        </div>
        <textarea
          className="flex-1 bg-transparent text-sm text-muted-foreground placeholder:text-muted-foreground/60 outline-none resize-none min-h-[48px]"
          placeholder="Note / remark…"
          value={line.notes ?? ""}
          onChange={(e) => onUpdate(line.id, { notes: e.target.value })}
          rows={2}
        />
        <button
          type="button"
          onClick={() => onRemove(line.id)}
          className="text-muted-foreground hover:text-destructive transition-colors mt-0.5"
        >
          <Trash2 className="h-4 w-4" />
        </button>
      </div>
    );
  }

  // Product line
  return (
    <div
      className={cn(
        "rounded-xl border border-border bg-card transition-shadow",
        isDragging && "opacity-50 shadow-2xl"
      )}
    >
      {/* Header row */}
      <div className="flex items-center gap-2 px-3 py-2.5 border-b border-border">
        <div {...(dragHandleProps as object)} className="cursor-grab touch-none">
          <GripVertical className="h-4 w-4 text-muted-foreground" />
        </div>

        <span className="w-5 text-xs text-muted-foreground font-mono">{index + 1}</span>

        <div className="flex-1 min-w-0">
          <span className="text-sm font-medium text-foreground truncate">
            {line.product_code
              ? `${line.product_code} — ${line.product_name ?? ""}`
              : "Select product…"}
          </span>
        </div>

        {/* Line total */}
        <span className="text-sm font-semibold text-foreground whitespace-nowrap">
          {line.line_total_egp != null
            ? `EGP ${line.line_total_egp.toLocaleString("en-EG", { minimumFractionDigits: 2 })}`
            : "—"}
        </span>

        <button
          type="button"
          onClick={() => setExpanded((e) => !e)}
          className="text-muted-foreground hover:text-foreground transition-colors"
        >
          {expanded ? (
            <ChevronUp className="h-4 w-4" />
          ) : (
            <ChevronDown className="h-4 w-4" />
          )}
        </button>

        <button
          type="button"
          onClick={() => onRemove(line.id)}
          className="text-muted-foreground hover:text-destructive transition-colors"
        >
          <Trash2 className="h-4 w-4" />
        </button>
      </div>

      {/* Expanded fields */}
      {expanded && (
        <div className="p-3 grid grid-cols-2 lg:grid-cols-4 gap-3">
          {/* Qty */}
          <div className="flex flex-col gap-1">
            <label className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
              Qty
            </label>
            <input
              type="number"
              min={0}
              step="0.0001"
              value={line.quantity ?? ""}
              onChange={(e) =>
                onUpdate(line.id, { quantity: parseFloat(e.target.value) || 0 })
              }
              className="w-full rounded-lg border border-border bg-background px-3 py-1.5 text-sm outline-none focus:ring-2 focus:ring-gamma-blue/40"
              placeholder="0"
            />
          </div>

          {/* UOM */}
          <div className="flex flex-col gap-1">
            <label className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
              UOM
            </label>
            <input
              type="text"
              value={line.unit_of_measure ?? "pcs"}
              onChange={(e) =>
                onUpdate(line.id, { unit_of_measure: e.target.value })
              }
              className="w-full rounded-lg border border-border bg-background px-3 py-1.5 text-sm outline-none focus:ring-2 focus:ring-gamma-blue/40"
            />
          </div>

          {/* Unit price (foreign) */}
          <div className="flex flex-col gap-1">
            <label className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
              Unit Price
            </label>
            <div className="flex rounded-lg border border-border overflow-hidden focus-within:ring-2 focus-within:ring-gamma-blue/40">
              <select
                value={line.currency ?? "USD"}
                onChange={(e) => onUpdate(line.id, { currency: e.target.value })}
                className="bg-muted text-xs px-2 border-r border-border outline-none"
              >
                {currencies.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
              <input
                type="number"
                min={0}
                step="0.0001"
                value={line.unit_price_foreign ?? ""}
                onChange={(e) =>
                  onUpdate(line.id, {
                    unit_price_foreign: parseFloat(e.target.value) || 0,
                  })
                }
                className="flex-1 bg-background px-3 py-1.5 text-sm outline-none"
                placeholder="0.00"
              />
            </div>
          </div>

          {/* Discount */}
          <div className="flex flex-col gap-1">
            <label className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
              Discount %
            </label>
            <input
              type="number"
              min={0}
              max={100}
              step="0.01"
              value={line.discount_pct ?? ""}
              onChange={(e) =>
                onUpdate(line.id, {
                  discount_pct: parseFloat(e.target.value) || 0,
                })
              }
              className="w-full rounded-lg border border-border bg-background px-3 py-1.5 text-sm outline-none focus:ring-2 focus:ring-gamma-blue/40"
              placeholder="0"
            />
          </div>

          {/* Notes — full width */}
          <div className="col-span-2 lg:col-span-4 flex flex-col gap-1">
            <label className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
              Line Notes
            </label>
            <input
              type="text"
              value={line.notes ?? ""}
              onChange={(e) => onUpdate(line.id, { notes: e.target.value })}
              className="w-full rounded-lg border border-border bg-background px-3 py-1.5 text-sm outline-none focus:ring-2 focus:ring-gamma-blue/40"
              placeholder="Optional note…"
            />
          </div>
        </div>
      )}
    </div>
  );
}
