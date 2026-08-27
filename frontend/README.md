# ITCA Frontend (standalone)

This is just the frontend — for when you're building the UI independently
of your team's backend work. It can run two ways:

## Option 1: Against the mock API (no backend needed at all)

Good for building/demoing your UI today, before the real backend is ready.

```bash
# terminal 1 - fake API with realistic sample data
cd mock-server
npm install
npm start          # http://localhost:4000

# terminal 2 - the actual UI
cd frontend
npm install
npm run dev         # http://localhost:5173
```

Open http://localhost:5173. Everything works — CRUD, dashboard, reports —
just against in-memory fake data instead of a real database. Restarting
the mock server resets the data back to its seed state.

## Option 2: Against your team's real backend

Once your teammates have their API running (wherever it's hosted — their
laptop, a shared dev server, whatever), point the frontend at it instead:

Open `frontend/vite.config.js` and change:

```js
proxy: {
  '/api': {
    target: 'http://localhost:4000',   // <- change this
    changeOrigin: true,
  },
},
```

to their backend's URL. As long as their API matches `API_CONTRACT.md`,
nothing else in the frontend needs to change — same components, same
`src/api.js`, same everything. That's the whole point of building against
a contract instead of a specific implementation.

## What's in here

- `API_CONTRACT.md` — the interface your backend team needs to implement.
  Share this with them / agree on it together before they start, so you're
  not building against a moving target.
- `mock-server/` — throwaway fake API, **not meant to be your real
  deliverable**. It's an in-memory stand-in so you're not blocked. Delete
  it once the real backend exists, or keep it around for your own
  frontend-only testing/demos.
- `frontend/` — the actual UI you're responsible for. See `frontend/src/config/entities.js`
  for how each table's fields/labels/form types are defined, and
  `frontend/src/pages/` for the two page types (generic CRUD page, and
  the reports dashboard).

## Design notes for your report

The UI is config-driven: `frontend/src/config/entities.js` describes every
table once (fields, labels, foreign keys), and generic `DataTable` /
`EntityForm` components render CRUD screens for whichever entity you point
them at. Adding a new manageable field or table is a config change, not
new component code. Styling follows a "certification ledger" theme — navy
+ brass-gold, serif headings, monospace IDs, small stamped "seal" badges
for status values — defined centrally in `frontend/src/styles.css`.
