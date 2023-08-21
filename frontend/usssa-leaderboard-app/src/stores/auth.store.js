import { defineStore } from 'pinia';

import axios from 'axios';
import router from '@/router'

const baseUrl = process.env.VUE_APP_LEADERBOARD_API_URL;

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        user: JSON.parse(localStorage.getItem('user')),
        returnUrl: null
    }),
    actions: {
        async login(username, password) {
            const params = new URLSearchParams()
            params.append("username", username)
            params.append("password", password)
            const user = await axios
                .post(`${baseUrl}/token`, params)
                .then(response => {
                    console.log(response.data);
                    // TODO event bus the leaderboard
                    //this.category_results = response.data.category_results
                    return response.data;
                });

            // update pinia state
            this.user = user;

            // store user details and jwt in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(user));

            // redirect to previous url or default to home page
            router.push(this.returnUrl || '/');
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
            router.push('/login');
        }
    }
});