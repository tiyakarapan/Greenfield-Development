export default function Modal({ title, onClose, children, footer }) {
  return (
    <div className="modal-backdrop" onMouseDown={(e) => { if (e.target === e.currentTarget) onClose(); }}>
      <div className="modal">
        <div className="modal-header">
          <h2>{title}</h2>
          <button className="btn-ghost" onClick={onClose} aria-label="Close">✕</button>
        </div>
        {children}
        {footer && <div className="modal-footer">{footer}</div>}
      </div>
    </div>
  );
}
