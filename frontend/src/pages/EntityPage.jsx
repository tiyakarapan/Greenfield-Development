import { useEffect, useState, useCallback } from 'react';
import { entities } from '../config/entities';
import { api, apiErrorMessage } from '../api';
import DataTable from '../components/DataTable';
import Modal from '../components/Modal';
import EntityForm from '../components/EntityForm';

export default function EntityPage({ entityKey, onDataChanged }) {
  const config = entities[entityKey];

  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [fkOptions, setFkOptions] = useState({});
  const [modalMode, setModalMode] = useState(null); // 'create' | 'edit' | null
  const [editingRow, setEditingRow] = useState(null);

  const fkKeys = [...new Set(config.fields.filter((f) => f.type === 'fk').map((f) => f.fk))];

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [rowData, ...fkData] = await Promise.all([
        api.list(entityKey),
        ...fkKeys.map((k) => api.list(k)),
      ]);
      setRows(rowData);
      const fkMap = {};
      fkKeys.forEach((k, i) => { fkMap[k] = fkData[i]; });
      setFkOptions(fkMap);
    } catch (err) {
      setError(apiErrorMessage(err));
    } finally {
      setLoading(false);
    }
  }, [entityKey]);

  useEffect(() => { load(); }, [load]);

  async function handleSubmit(payload) {
    if (modalMode === 'edit') {
      const idVal = config.pk.map((p) => editingRow[p]).join('_');
      await api.update(entityKey, idVal, payload);
    } else {
      await api.create(entityKey, payload);
    }
    setModalMode(null);
    setEditingRow(null);
    await load();
    onDataChanged?.();
  }

  async function handleDelete(row) {
    const label = config.displayField(row);
    if (!window.confirm(`Delete ${config.singular.toLowerCase()} "${label}"? This cannot be undone.`)) return;
    try {
      const idVal = config.pk.map((p) => row[p]).join('_');
      await api.remove(entityKey, idVal);
      await load();
      onDataChanged?.();
    } catch (err) {
      alert(apiErrorMessage(err));
    }
  }

  return (
    <div>
      <div className="page-header">
        <div>
          <h1 className="page-title">{config.label}</h1>
          <div className="page-subtitle">{rows.length} record{rows.length === 1 ? '' : 's'}</div>
        </div>
        <button className="btn btn-primary" onClick={() => { setModalMode('create'); setEditingRow(null); }}>
          + Add {config.singular}
        </button>
      </div>

      {error && <div className="error-banner">{error}</div>}
      {loading ? (
        <div className="loading">Loading…</div>
      ) : (
        <DataTable
          config={config}
          rows={rows}
          onEdit={(row) => { setEditingRow(row); setModalMode('edit'); }}
          onDelete={handleDelete}
        />
      )}

      {modalMode && (
        <Modal
          title={modalMode === 'edit' ? `Edit ${config.singular}` : `Add ${config.singular}`}
          onClose={() => { setModalMode(null); setEditingRow(null); }}
        >
          <EntityForm
            config={config}
            initial={modalMode === 'edit' ? editingRow : null}
            fkOptions={fkOptions}
            onSubmit={handleSubmit}
            onCancel={() => { setModalMode(null); setEditingRow(null); }}
            submitLabel={modalMode === 'edit' ? 'Save changes' : 'Create'}
          />
        </Modal>
      )}
    </div>
  );
}
