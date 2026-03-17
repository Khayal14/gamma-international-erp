"use client";

import { ReactNode, useState } from "react";
import { cn } from "@/lib/utils";
import { Check, ChevronLeft, ChevronRight, Loader2 } from "lucide-react";

// ─── Step definition ──────────────────────────────────────────────────────────

export interface FormStep {
  id: string;
  title: string;
  /** Short label used in the progress bar */
  shortTitle?: string;
  description?: string;
  /** The step content — form fields, etc. */
  content: ReactNode;
  /**
   * Async validator called before advancing.
   * Return true to proceed, false (or throw) to stay on step.
   */
  validate?: () => Promise<boolean> | boolean;
}

// ─── Props ────────────────────────────────────────────────────────────────────

interface StepFormProps {
  steps: FormStep[];
  /** Called when the final step's "Submit" is confirmed */
  onSubmit: () => Promise<void> | void;
  /** Label for the final submit button */
  submitLabel?: string;
  /** If true, disables all navigation */
  disabled?: boolean;
  className?: string;
}

// ─── Step indicator ───────────────────────────────────────────────────────────

function StepIndicator({
  steps,
  current,
  onNavigate,
}: {
  steps: FormStep[];
  current: number;
  onNavigate: (index: number) => void;
}) {
  return (
    <div className="flex items-center gap-0 w-full mb-6 overflow-x-auto pb-1">
      {steps.map((step, idx) => {
        const isCompleted = idx < current;
        const isCurrent = idx === current;
        const isClickable = idx < current;

        return (
          <div key={step.id} className="flex items-center flex-1 min-w-0">
            {/* Step circle */}
            <button
              type="button"
              disabled={!isClickable}
              onClick={() => isClickable && onNavigate(idx)}
              className={cn(
                "flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold transition-all",
                isCompleted &&
                  "bg-gamma-blue text-white cursor-pointer hover:bg-gamma-blue/80",
                isCurrent &&
                  "bg-gamma-gold text-gamma-dark ring-4 ring-gamma-gold/20",
                !isCompleted &&
                  !isCurrent &&
                  "bg-muted text-muted-foreground cursor-not-allowed"
              )}
            >
              {isCompleted ? (
                <Check className="h-4 w-4" />
              ) : (
                <span>{idx + 1}</span>
              )}
            </button>

            {/* Step label (hidden on very small screens) */}
            <span
              className={cn(
                "hidden sm:block ml-2 text-xs font-medium truncate max-w-[80px]",
                isCurrent ? "text-foreground" : "text-muted-foreground"
              )}
            >
              {step.shortTitle ?? step.title}
            </span>

            {/* Connector line */}
            {idx < steps.length - 1 && (
              <div
                className={cn(
                  "flex-1 h-0.5 mx-2 rounded-full transition-colors",
                  idx < current ? "bg-gamma-blue" : "bg-border"
                )}
              />
            )}
          </div>
        );
      })}
    </div>
  );
}

// ─── Component ───────────────────────────────────────────────────────────────

export function StepForm({
  steps,
  onSubmit,
  submitLabel = "Submit",
  disabled = false,
  className,
}: StepFormProps) {
  const [current, setCurrent] = useState(0);
  const [submitting, setSubmitting] = useState(false);
  const [validating, setValidating] = useState(false);

  const isFirst = current === 0;
  const isLast = current === steps.length - 1;
  const step = steps[current];

  async function handleNext() {
    if (validating) return;
    if (step.validate) {
      setValidating(true);
      try {
        const ok = await step.validate();
        if (!ok) return;
      } catch {
        return;
      } finally {
        setValidating(false);
      }
    }
    if (isLast) {
      setSubmitting(true);
      try {
        await onSubmit();
      } finally {
        setSubmitting(false);
      }
    } else {
      setCurrent((c) => c + 1);
    }
  }

  function handleBack() {
    if (!isFirst) setCurrent((c) => c - 1);
  }

  function navigateTo(index: number) {
    if (index < current) setCurrent(index);
  }

  return (
    <div className={cn("flex flex-col", className)}>
      {/* Progress indicator */}
      <StepIndicator steps={steps} current={current} onNavigate={navigateTo} />

      {/* Step header */}
      <div className="mb-4">
        <h2 className="text-lg font-semibold text-foreground">{step.title}</h2>
        {step.description && (
          <p className="text-sm text-muted-foreground mt-0.5">
            {step.description}
          </p>
        )}
      </div>

      {/* Step content — grows to fill available space */}
      <div className="flex-1 min-h-0">{step.content}</div>

      {/* Navigation footer */}
      <div className="flex items-center justify-between pt-6 mt-6 border-t border-border">
        <button
          type="button"
          onClick={handleBack}
          disabled={isFirst || disabled || submitting}
          className={cn(
            "flex items-center gap-1.5 px-4 py-2 rounded-lg text-sm font-medium transition-colors",
            "border border-border hover:bg-muted",
            (isFirst || disabled || submitting) &&
              "opacity-40 cursor-not-allowed pointer-events-none"
          )}
        >
          <ChevronLeft className="h-4 w-4" />
          Back
        </button>

        {/* Step count badge (mobile) */}
        <span className="text-xs text-muted-foreground sm:hidden">
          {current + 1} / {steps.length}
        </span>

        <button
          type="button"
          onClick={handleNext}
          disabled={disabled || submitting || validating}
          className={cn(
            "flex items-center gap-1.5 px-5 py-2 rounded-lg text-sm font-semibold transition-colors",
            "bg-gamma-blue text-white hover:bg-gamma-blue/90",
            (disabled || submitting || validating) &&
              "opacity-60 cursor-not-allowed pointer-events-none"
          )}
        >
          {submitting || validating ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : isLast ? (
            submitLabel
          ) : (
            <>
              Next
              <ChevronRight className="h-4 w-4" />
            </>
          )}
        </button>
      </div>
    </div>
  );
}
