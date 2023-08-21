import { defineStore } from 'pinia';

import axios from 'axios';
import { authHeader } from '@/helpers/axiosHelper';

const baseUrl = process.env.VUE_APP_LEADERBOARD_API_URL;

export const useCounterStore = defineStore('counter', {
    state: () => ({ count: 0, name: 'Eduardo' }),
    getters: {
      doubleCount: (state) => state.count * 2,
    },
    actions: {
      increment() {
        this.count++
      },
    },
  })


export const useLeaderboardsStore = defineStore({
    id: 'leaderboards',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        leaderboards: JSON.parse(localStorage.getItem('leaderboards')),
        // returnUrl: null
        returnUrl: null
    }),
    actions: {
        async getAll() {
            // Gets all leaderboards
            const leaderboards = await axios
                .get(`${baseUrl}/leaderboards`)
                .then(response => {
                    // TODO event bus the leaderboard
                    //this.category_results = response.data.category_results
                    return response.data;
                });

            // update pinia state
            this.leaderboards = leaderboards;

            // store user details and jwt in local storage to keep user logged in between page refreshes
            localStorage.setItem('leaderboards', JSON.stringify(leaderboards));

            // redirect to previous url or default to home page
            //router.push(this.returnUrl || '/');
        },
        async create(name, description, awardValues, categories) {
            const headers = authHeader(baseUrl);

            let eventData = {
                name: name,
                description: description,
                award_values: awardValues,
                categories: categories,
                contingents: []
            }

            let data = await axios
                .post(`${baseUrl}/leaderboards`, eventData, {headers})
                .then(response => {
                    console.log(response.data);
                    // TODO event bus the leaderboard
                    // this.category_results = response.data.category_results
                    //this.getAll()
                    return response.data;
                });
            
            this.getAll()
            
            return data;
        },

        async getLeaderboard(leaderboardSlug) {
            let data = await axios
                .get(`${baseUrl}/leaderboards/${leaderboardSlug}`)
                .then(response => { 
                    let leaderboard = response.data; 
                    if (leaderboard.categories == null) {
                        leaderboard.categories = []
                    }
                    if (leaderboard.category_results == null) {
                        leaderboard.category_results = []
                    }
                    if (leaderboard.contingents == null) {
                        leaderboard.contingents = []
                    }
                    leaderboard.idToContingent = Object.fromEntries(
                        leaderboard.contingents.map(c => [c.id, c])
                    );
                    return leaderboard;
                });
            console.log("DAYDAYDAYDAYTA")
            console.log(data)
            return data;
        },

        async addContingents(leaderboard_slug, contingentsBatchData) {
            const headers = authHeader(baseUrl);

            let data = await axios
                .post(`${baseUrl}/leaderboards/${leaderboard_slug}/contingents/batch`, 
                    contingentsBatchData,
                    { headers })
                .then(response => {
                    // TODO event bus the leaderboard
                    // this.category_results = response.data.category_results
                    return response.data;
                });
            this.getAll();
            return data
        },

        async addCategoryResults(leaderboard_slug, resultsData) {
            const headers = authHeader(baseUrl);

            let data = await axios
                .post(`${baseUrl}/leaderboards/${leaderboard_slug}/category_results`, 
                    resultsData,
                    { headers })
                .then(response => {
                    console.log(response.data); // TODO event bus the leaderboard //this.category_results = response.data.category_results return response.data;
                });
            return data;
        }
    }
});