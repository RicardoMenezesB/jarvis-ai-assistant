html, body, #root {
  margin: 0;
  min-height: 100%;
  height: 100%;
  font-family: 'Inter', sans-serif;
  background:
    radial-gradient(circle at top left, rgba(96, 165, 250, 0.18), transparent 30%),
    radial-gradient(circle at bottom right, rgba(45, 212, 191, 0.14), transparent 25%),
    #060b14;
  color: #e6edf7;
}

* {
  box-sizing: border-box;
}

button, input {
  font: inherit;
}

.app-shell {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 24px;
  height: 100%;
  padding: 24px;
}

.panel {
  background: rgba(10, 18, 31, 0.82);
  border: 1px solid rgba(148, 163, 184, 0.12);
  box-shadow: 0 12px 36px rgba(14, 25, 43, 0.3);
  backdrop-filter: blur(18px);
  border-radius: 24px;
}

.sidebar {
  padding: 22px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.brand-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-mark {
  width: 58px;
  height: 58px;
  display: grid;
  place-items: center;
  border-radius: 18px;
  background: linear-gradient(135deg, #38bdf8, #22c55e);
  color: #03131e;
  font-weight: 800;
  font-size: 1.2rem;
}

h1, h2, h3, p {
  margin: 0;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.7rem;
  opacity: 0.7;
}

.status-box {
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1px solid rgba(56, 189, 248, 0.2);
  background: rgba(10, 14, 26, 0.7);
  border-radius: 12px;
  padding: 12px 14px;
  color: #dbeafe;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: #22c55e;
  box-shadow: 0 0 12px rgba(34, 197, 94, 0.9);
}

.shortcut-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.shortcut-button {
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.12);
  color: #e2e8f0;
  border-radius: 12px;
  padding: 12px 14px;
  text-align: left;
  cursor: pointer;
  transition: transform 0.18s ease, border-color 0.18s ease;
}

.shortcut-button:hover {
  transform: translateY(-1px);
  border-color: rgba(96, 165, 250, 0.5);
}

.metrics {
  margin-top: auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.metric-card {
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: 14px;
  padding: 12px 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.metric-card span {
  font-size: 0.72rem;
  text-transform: uppercase;
  opacity: 0.7;
}

.metric-card strong {
  font-size: 1rem;
}

.main-panel {
  display: flex;
  flex-direction: column;
  min-height: 0;
  padding: 18px;
}

.header-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.toolbar {
  display: flex;
  gap: 10px;
}

.secondary-button,
.voice-button,
.composer button {
  border: 0;
  border-radius: 12px;
  padding: 10px 14px;
  cursor: pointer;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.secondary-button {
  background: rgba(15, 23, 42, 0.8);
  color: #e2e8f0;
  border: 1px solid rgba(148, 163, 184, 0.15);
}

.voice-button {
  background: linear-gradient(135deg, #0ea5e9, #06b6d4);
  color: #03131e;
  font-weight: 700;
}

.voice-button.active {
  background: linear-gradient(135deg, #22c55e, #14b8a6);
}

.chat-window {
  flex: 1;
  background: rgba(15, 23, 42, 0.35);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: 18px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  overflow: auto;
}

.message-row {
  display: flex;
}

.message-row.user {
  justify-content: flex-end;
}

.bubble {
  max-width: min(72%, 560px);
  padding: 12px 14px;
  border-radius: 16px;
  background: rgba(14, 116, 144, 0.12);
  border: 1px solid rgba(96, 165, 250, 0.15);
}

.message-row.user .bubble {
  background: linear-gradient(135deg, rgba(14, 165, 233, 0.25), rgba(34, 197, 94, 0.18));
}

.bubble small {
  display: block;
  margin-bottom: 6px;
  opacity: 0.75;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.bubble p {
  line-height: 1.6;
  white-space: pre-wrap;
}

.loading-bubble {
  display: flex;
  align-items: center;
  gap: 10px;
}

.pulse {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: #7dd3fc;
  display: inline-block;
  animation: pulse 1.2s infinite ease-in-out;
}

@keyframes pulse {
  0% { transform: scale(0.9); opacity: 0.7; }
  50% { transform: scale(1.25); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.7; }
}

.composer {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  margin-top: 16px;
}

.composer input {
  background: rgba(15, 23, 42, 0.75);
  border: 1px solid rgba(148, 163, 184, 0.14);
  color: #e2e8f0;
  border-radius: 14px;
  padding: 15px 16px;
  outline: none;
}

.composer input:focus {
  border-color: rgba(96, 165, 250, 0.7);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.14);
}

.composer button {
  background: linear-gradient(135deg, #60a5fa, #34d399);
  color: #03131e;
  font-weight: 700;
}

.search-panel {
  margin-top: 18px;
  display: grid;
  gap: 10px;
}

.search-card {
  display: block;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-radius: 14px;
  padding: 12px 14px;
  color: #e2e8f0;
  text-decoration: none;
}

.search-card strong {
  display: block;
  margin-bottom: 6px;
}

.search-card span {
  opacity: 0.76;
  line-height: 1.5;
}

@media (max-width: 900px) {
  .app-shell {
    display: block;
  }

  .sidebar {
    margin-bottom: 20px;
  }
}

@media (max-width: 560px) {
  .app-shell {
    padding: 14px;
  }

  .composer {
    grid-template-columns: 1fr;
  }

  .metrics {
    grid-template-columns: 1fr;
  }

  .bubble {
    max-width: 100%;
  }
}
