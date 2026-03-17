import { create } from "zustand";
import { apiClient } from "@/lib/api/client";

interface AuthState {
  user: any | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isLoading: false,

  login: async (email, password) => {
    set({ isLoading: true });
    try {
      const { data } = await apiClient.post("/auth/login", { email, password });
      localStorage.setItem("access_token", data.access_token);
      localStorage.setItem("refresh_token", data.refresh_token);
      const me = await apiClient.get("/users/me");
      set({ user: me.data, isLoading: false });
      window.location.href = "/dashboard";
    } finally {
      set({ isLoading: false });
    }
  },

  logout: () => {
    localStorage.clear();
    set({ user: null });
    window.location.href = "/login";
  },
}));
