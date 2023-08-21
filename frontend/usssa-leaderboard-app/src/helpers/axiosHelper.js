import { useAuthStore } from '@/stores/auth.store'

const baseUrl = process.env.VUE_APP_LEADERBOARD_API_URL;

export function authHeader(url) {
    // return auth header with jwt if user is logged in and request is to the api url
    const { user } = useAuthStore();
    const isLoggedIn = !!user?.access_token;
    const isApiUrl = url.startsWith(baseUrl)
    if (isLoggedIn && isApiUrl) {
        return { Authorization: `Bearer ${user.access_token}` };
    } else {
        return {};
    }
}