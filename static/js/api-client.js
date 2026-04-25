/**
 * Career Advisor API Client
 * Provides JavaScript interface to all REST API endpoints
 */

class CareerAdvisorAPI {
    constructor(baseURL = '/api') {
        this.baseURL = baseURL;
        this.headers = { 'Content-Type': 'application/json' };
    }

    /**
     * Get all colleges with optional filters and pagination
     */
    async getColleges(params = {}) {
        try {
            const queryString = new URLSearchParams(params).toString();
            const url = `${this.baseURL}/colleges${queryString ? '?' + queryString : ''}`;
            const response = await fetch(url);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching colleges:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Get single college by ID
     */
    async getCollege(id) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/${id}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching college:', error);
            return { error: error.message };
        }
    }

    /**
     * Search colleges by query
     */
    async searchColleges(query) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/search?query=${encodeURIComponent(query)}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error searching colleges:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Filter colleges by multiple criteria
     */
    async filterColleges(filters) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/filter`, {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(filters)
            });
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error filtering colleges:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Get colleges by city
     */
    async getCollegesByCity(city) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/by-city/${encodeURIComponent(city)}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching colleges by city:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Get colleges by stream
     */
    async getCollegesByStream(stream) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/by-stream/${encodeURIComponent(stream)}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching colleges by stream:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Get colleges by degree
     */
    async getCollegesByDegree(degree) {
        try {
            const response = await fetch(`${this.baseURL}/colleges/by-degree/${encodeURIComponent(degree)}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching colleges by degree:', error);
            return { colleges: [], error: error.message };
        }
    }

    /**
     * Get college statistics
     */
    async getStatistics() {
        try {
            const response = await fetch(`${this.baseURL}/colleges/stats`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('Error fetching statistics:', error);
            return { error: error.message };
        }
    }

    /**
     * Health check
     */
    async healthCheck() {
        try {
            const response = await fetch(`${this.baseURL}/health`);
            return { status: response.ok ? 'ok' : 'error' };
        } catch (error) {
            return { status: 'error', error: error.message };
        }
    }
}

// Initialize global API instance
const API = new CareerAdvisorAPI('/api');
