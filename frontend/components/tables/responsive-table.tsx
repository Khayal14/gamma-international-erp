"use client";

import { ReactNode } from "react";
import { cn } from "@/lib/utils";
import { ChevronRight } from "lucide-react";

// ─── Column definition ────────────────────────────────────────────────────────

export interface Column<T> {
  key: string;
  header: string;
  /** Render function for the cell value */
  cell: (row: T) => ReactNode;
  /** If true, this column is hidden on mobile card view (shown only in table) */
  hideOnMobile?: boolean;
  /** Column header class (e.g. text alignment) */
  headerClass?: string;
  /** Cell class */
  cellClass?: string;
}

// ─── Card field definition ────────────────────────────────────────────────────

export interface CardField<T> {
  /** Label shown on the card */
  label: string;
  /** Render function */
  value: (row: T) => ReactNode;
  /** If true, renders as a badge-style chip */
  badge?: boolean;
}

// ─── Props ────────────────────────────────────────────────────────────────────

interface ResponsiveTableProps<T> {
  /** Row data */
  data: T[];
  /** Column definitions for the desktop table */
  columns: Column<T>[];
  /**
   * Card field definitions for the mobile card list.
   * If omitted, falls back to non-hidden columns.
   */
  cardFields?: CardField<T>[];
  /** Unique key extractor */
  rowKey: (row: T) => string;
  /** Optional click handler — adds a chevron on mobile cards */
  onRowClick?: (row: T) => void;
  /** Show a loading skeleton */
  loading?: boolean;
  /** Empty state message */
  emptyMessage?: string;
  /** Primary label for each mobile card (bold, top-left) */
  cardTitle?: (row: T) => ReactNode;
  /** Secondary label for each mobile card (muted, top-right) */
  cardSubtitle?: (row: T) => ReactNode;
  className?: string;
}

// ─── Skeleton helpers ────────────────────────────────────────────────────────

function TableSkeleton({ cols }: { cols: number }) {
  return (
    <>
      {Array.from({ length: 5 }).map((_, i) => (
        <tr key={i} className="border-b border-border animate-pulse">
          {Array.from({ length: cols }).map((_, j) => (
            <td key={j} className="px-4 py-3">
              <div className="h-4 bg-muted rounded w-3/4" />
            </td>
          ))}
        </tr>
      ))}
    </>
  );
}

function CardSkeleton() {
  return (
    <>
      {Array.from({ length: 4 }).map((_, i) => (
        <div
          key={i}
          className="rounded-xl border border-border p-4 space-y-2 animate-pulse"
        >
          <div className="flex justify-between">
            <div className="h-4 bg-muted rounded w-1/3" />
            <div className="h-4 bg-muted rounded w-1/4" />
          </div>
          <div className="h-3 bg-muted rounded w-2/3" />
          <div className="h-3 bg-muted rounded w-1/2" />
        </div>
      ))}
    </>
  );
}

// ─── Component ───────────────────────────────────────────────────────────────

export function ResponsiveTable<T>({
  data,
  columns,
  cardFields,
  rowKey,
  onRowClick,
  loading = false,
  emptyMessage = "No records found.",
  cardTitle,
  cardSubtitle,
  className,
}: ResponsiveTableProps<T>) {
  const mobileFields: CardField<T>[] =
    cardFields ??
    columns
      .filter((c) => !c.hideOnMobile)
      .map((c) => ({ label: c.header, value: c.cell }));

  return (
    <div className={cn("w-full", className)}>
      {/* ── Desktop table ──────────────────────────────────────────────── */}
      <div className="hidden lg:block overflow-x-auto rounded-xl border border-border">
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-muted/50 border-b border-border">
              {columns.map((col) => (
                <th
                  key={col.key}
                  className={cn(
                    "px-4 py-3 text-left font-medium text-muted-foreground whitespace-nowrap",
                    col.headerClass
                  )}
                >
                  {col.header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <TableSkeleton cols={columns.length} />
            ) : data.length === 0 ? (
              <tr>
                <td
                  colSpan={columns.length}
                  className="px-4 py-10 text-center text-muted-foreground"
                >
                  {emptyMessage}
                </td>
              </tr>
            ) : (
              data.map((row) => (
                <tr
                  key={rowKey(row)}
                  onClick={onRowClick ? () => onRowClick(row) : undefined}
                  className={cn(
                    "border-b border-border last:border-0 transition-colors",
                    onRowClick &&
                      "cursor-pointer hover:bg-muted/40"
                  )}
                >
                  {columns.map((col) => (
                    <td
                      key={col.key}
                      className={cn("px-4 py-3 align-middle", col.cellClass)}
                    >
                      {col.cell(row)}
                    </td>
                  ))}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* ── Mobile card list ───────────────────────────────────────────── */}
      <div className="lg:hidden space-y-3">
        {loading ? (
          <CardSkeleton />
        ) : data.length === 0 ? (
          <div className="py-10 text-center text-muted-foreground text-sm">
            {emptyMessage}
          </div>
        ) : (
          data.map((row) => (
            <div
              key={rowKey(row)}
              onClick={onRowClick ? () => onRowClick(row) : undefined}
              className={cn(
                "rounded-xl border border-border bg-card p-4 space-y-2 transition-colors",
                onRowClick && "cursor-pointer active:bg-muted/50"
              )}
            >
              {/* Card header row */}
              {(cardTitle || cardSubtitle || onRowClick) && (
                <div className="flex items-start justify-between gap-2">
                  <div className="flex-1 min-w-0">
                    {cardTitle && (
                      <div className="font-semibold text-foreground truncate">
                        {cardTitle(row)}
                      </div>
                    )}
                    {cardSubtitle && (
                      <div className="text-xs text-muted-foreground mt-0.5">
                        {cardSubtitle(row)}
                      </div>
                    )}
                  </div>
                  {onRowClick && (
                    <ChevronRight className="h-4 w-4 text-muted-foreground flex-shrink-0 mt-0.5" />
                  )}
                </div>
              )}

              {/* Card fields grid */}
              <div className="grid grid-cols-2 gap-x-4 gap-y-1.5">
                {mobileFields.map((field, idx) => (
                  <div key={idx} className="min-w-0">
                    <div className="text-[10px] font-medium text-muted-foreground uppercase tracking-wide">
                      {field.label}
                    </div>
                    <div className="text-sm text-foreground mt-0.5">
                      {field.value(row)}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
