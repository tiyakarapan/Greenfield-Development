// src/api.js
// Thin wrapper around axios so every screen talks to the backend the
// same way. Base URL is empty because vite.config.js proxies /api to
// the Express server during dev (see server block).
import axios from 'axios';

const client = axios.create({ baseURL: '/api' });

export const api = {
  list: (entity) => client.get(`/${entity}`).then((r) => r.data),
  get: (entity, id) => client.get(`/${entity}/${id}`).then((r) => r.data),
  create: (entity, data) => client.post(`/${entity}`, data).then((r) => r.data),
  update: (entity, id, data) => client.put(`/${entity}/${id}`, data).then((r) => r.data),
  remove: (entity, id) => client.delete(`/${entity}/${id}`).then((r) => r.data),
  report: (path, params) => client.get(`/reports/${path}`, { params }).then((r) => r.data),
};

// Pulls the error message our backend formats server-side (trigger /
// constraint messages) so forms can show something a non-technical
// user (Andre) can actually act on.
export function apiErrorMessage(err) {
  return err?.response?.data?.error || err?.message || 'Something went wrong.';
}
