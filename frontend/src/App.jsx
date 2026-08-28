import { useCallback, useEffect, useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import EntityPage from './pages/EntityPage';
import Dashboard from './pages/Dashboard';
import { entities } from './config/entities';
import { api } from './api';

export default function App() {
  const [counts, setCounts] = useState({});

  const refreshCounts = useCallback(async () => {
    const entries = await Promise.all(
      Object.keys(entities).map(async (key) => {
        try {
          const rows = await api.list(key);
          return [key, rows.length];
        } catch {
          return [key, 0];
        }
      })
    );
    setCounts(Object.fromEntries(entries));
  }, []);

  useEffect(() => { refreshCounts(); }, [refreshCounts]);

  return (
    <div className="shell">
      <Sidebar counts={counts} />
      <main className="main-outer">
        <div className="main-inner">
          <Routes>
            <Route path="/" element={<Dashboard counts={counts} />} />
            {Object.keys(entities).map((key) => (
              <Route
                key={key}
                path={`/${key}`}
                element={<EntityPage entityKey={key} onDataChanged={refreshCounts} />}
              />
            ))}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </main>
    </div>
  );
}
