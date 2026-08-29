class APIClient {
    static async request(endpoint, method = "GET", body = null) {
        const options = {
            method,
            headers: { "Content-Type": "application/json" }
        };
        if (body) options.body = JSON.stringify(body);

        const response = await fetch(endpoint, options);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || "API Request Failed");
        }
        return data;
    }

    static get(endpoint) { return this.request(endpoint, "GET"); }
    static post(endpoint, body) { return this.request(endpoint, "POST", body); }
}
