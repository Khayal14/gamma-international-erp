import { ReactNode } from "react";
import { cn } from "@/lib/utils";

type BadgeVariant =
  | "default"
  | "success"
  | "warning"
  | "destructive"
  | "info"
  | "muted"
  | "gold";

const variantClasses: Record<BadgeVariant, string> = {
  default: "bg-gamma-blue/10 text-gamma-blue border-gamma-blue/20",
  success: "bg-green-500/10 text-green-600 border-green-500/20 dark:text-green-400",
  warning: "bg-yellow-500/10 text-yellow-600 border-yellow-500/20 dark:text-yellow-400",
  destructive: "bg-red-500/10 text-red-600 border-red-500/20 dark:text-red-400",
  info: "bg-sky-500/10 text-sky-600 border-sky-500/20 dark:text-sky-400",
  muted: "bg-muted text-muted-foreground border-border",
  gold: "bg-gamma-gold/10 text-gamma-gold border-gamma-gold/30",
};

interface BadgeProps {
  children: ReactNode;
  variant?: BadgeVariant;
  className?: string;
}

export function Badge({ children, variant = "default", className }: BadgeProps) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium border",
        variantClasses[variant],
        className
      )}
    >
      {children}
    </span>
  );
}

// ─── Status → variant mapping helpers ─────────────────────────────────────────

const OFFER_STATUS_VARIANT: Record<string, BadgeVariant> = {
  DRAFT: "muted",
  SENT: "info",
  ACCEPTED: "success",
  REJECTED: "destructive",
  EXPIRED: "warning",
  REVISED: "gold",
};

const ORDER_STATUS_VARIANT: Record<string, BadgeVariant> = {
  PENDING: "warning",
  CONFIRMED: "info",
  IN_PRODUCTION: "gold",
  READY_TO_SHIP: "success",
  SHIPPED: "success",
  DELIVERED: "success",
  CANCELLED: "destructive",
};

const PAYMENT_STATUS_VARIANT: Record<string, BadgeVariant> = {
  UNPAID: "destructive",
  DEPOSIT_PAID: "warning",
  FULLY_PAID: "success",
};

const LEAD_STATUS_VARIANT: Record<string, BadgeVariant> = {
  NEW: "info",
  CONTACTED: "default",
  QUALIFIED: "gold",
  PROPOSAL_SENT: "warning",
  WON: "success",
  LOST: "destructive",
  ON_HOLD: "muted",
};

export function StatusBadge({ status, type }: { status: string; type: "offer" | "order" | "payment" | "lead" }) {
  const map =
    type === "offer"
      ? OFFER_STATUS_VARIANT
      : type === "order"
      ? ORDER_STATUS_VARIANT
      : type === "payment"
      ? PAYMENT_STATUS_VARIANT
      : LEAD_STATUS_VARIANT;

  const variant = map[status] ?? "muted";
  const label = status.replace(/_/g, " ");

  return <Badge variant={variant}>{label}</Badge>;
}
