import { NavLink } from 'react-router-dom';
import { entities, navGroups } from '../config/entities';

export default function Sidebar({ counts }) {
  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="brand-mark">ITCA</span>
        <span className="brand-sub">Campus Records</span>
      </div>

      <div className="nav-group">
        <div className="nav-group-title">Overview</div>
        <NavLink to="/" end className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}>
          Dashboard
        </NavLink>
      </div>

      {navGroups.map((group) => (
        <div className="nav-group" key={group.title}>
          <div className="nav-group-title">{group.title}</div>
          {group.items.map((key) => {
            const cfg = entities[key];
            return (
              <NavLink
                key={key}
                to={`/${key}`}
                className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
              >
                <span>{cfg.label}</span>
                <span className="count">{counts?.[key] ?? ''}</span>
              </NavLink>
            );
          })}
        </div>
      ))}
    </aside>
  );
}
