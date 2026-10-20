* {
  box-sizing: border-box;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  height: 100%;
  font-family: 'Inter', sans-serif;
  background:
    radial-gradient(circle at top left, rgba(34, 211, 238, 0.12), transparent 24%),
    radial-gradient(circle at bottom right, rgba(59, 130, 246, 0.14), transparent 20%),
    #040b13;
  color: #e6edf7;
}

button, input, select {
  font: inherit;
}

.jarvis-app {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 24px;
  height: 100%;
  padding: 24px;
}

.glass-panel {
  background: rgba(8, 15, 25, 0.82);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 26px;
  box-shadow: 0 25px 60px rgba(3, 7, 18, 0.7), inset 0 0 0 1px rgba(255,255,255,0.02);
  backdrop-filter: blur(18px);
}

.sidebar {
  padding: 22px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.brand-block {
  display: flex;
  align-items: center;
  gap: 14px;
}

.brand-mark {
  width: 62px;
  height: 62px;
  display: grid;
  place-items: center;
  border-radius: 18px;
  background: linear-gradient(135deg, #7dd3fc, #22c55e);
  color: #061822;
  font-weight: 900;
  letter-spacing: 0.08em;
}

h1, h2, h3, p {
  margin: 0;
}

.eyebrow {
  font-size: 0.7rem;
  letter-spacing: 0.17em;
  text-transform: uppercase;
  opacity: 0.7;
}

.system-pill {
  display: flex;
  align-items: center;
  gap: 10px;
  border-radius: 14px;
  padding: 12px 14px;
  background: rgba(15, 23, 42, 0.72);
  border: 1px solid rgba(96, 165, 250, 0.2);
  color: #dbeafe;
}

.pulse-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #34d399;
  box-shadow: 0 0 12px rgba(52, 211, 153, 0.9);
  animation: blink 1.3s infinite ease-in-out;
}

@keyframes blink {
  0%, 100% { opacity: 0.7; transform: scale(0.9); }
  50% { opacity: 1; transform: scale(1.2); }
}

.quick-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.action-btn {
  width: 100%;
  padding: 12px 14px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.12);
  border-radius: 12px;
  text-align: left;
  color: #e2e8f0;
  cursor: pointer;
  transition: transform 0.18s ease, border-color 0.18s ease;
}

.action-btn:hover {
  transform: translateY(-1px);
  border-color: rgba(125, 211, 252, 0.5);
}

.metrics-grid {
  margin-top: auto;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 10px;
}

.metric-box {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 12px 10px;
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.86);
  border: 1px solid rgba(148, 163, 184, 0.12);
}

.metric-box span {
  font-size: 0.7rem;
  text-transform: uppercase;
  opacity: 0.7;
}

.metric-box strong {
  font-size: 0.95rem;
}

.main-panel {
  display: flex;
  flex-direction: column;
  padding: 18px;
  min-height: 0;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.toolbar {
  display: flex;
  align-items: center;
  gap: 10px;
}

.ghost-btn,
.voice-btn,
.composer button,
.primary-btn {
  border: 0;
  border-radius: 12px;
  padding: 10px 14px;
  cursor: pointer;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.ghost-btn {
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(148, 163, 184, 0.12);
  color: #e2e8f0;
}

.primary-btn {
  background: linear-gradient(135deg, #60a5fa, #34d399);
  color: #04141d;
  font-weight: 700;
}

.voice-btn {
  background: linear-gradient(135deg, #38bdf8, #22c55e);
  color: #04141d;
  font-weight: 700;
}

.voice-btn.active {
  background: linear-gradient(135deg, #22c55e, #14b8a6);
}

.hud-panel {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px 18px;
  border-radius: 18px;
  border: 1px solid rgba(96, 165, 250, 0.18);
  background: rgba(12, 18, 27, 0.7);
  margin-bottom: 16px;
}

.hud-ring {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  background: radial-gradient(circle at center, rgba(34, 211, 238, 0.14), rgba(15, 23, 42, 0.8) 58%, rgba(12, 18, 27, 1) 70%);
  display: grid;
  place-items: center;
  border: 1px solid rgba(125, 211, 252, 0.3);
  box-shadow: inset 0 0 30px rgba(59, 130, 246, 0.22), 0 0 22px rgba(34, 211, 238, 0.18);
}

.hud-core {
  width: 76px;
  height: 76px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at center, rgba(59,130,246,0.32), rgba(10,14,22,0.9));
  border: 1px solid rgba(125,211,252,0.3);
  text-transform: uppercase;
  font-size: 0.54rem;
  text-align: center;
  line-height: 1.1;
}

.hud-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.hud-info small {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  opacity: 0.7;
}

.config-panel {
  margin-bottom: 16px;
  padding: 16px;
  border-radius: 18px;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.14);
}

.config-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.config-grid label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 0.8rem;
  opacity: 0.9;
}

.config-grid input,
.config-grid select {
  width: 100%;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 10px;
  color: #e2e8f0;
  padding: 10px 12px;
}

.config-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 14px;
}

.chat-window {
  flex: 1;
  background: rgba(15, 23, 42, 0.38);
  border: 1px solid rgba(148, 163, 184, 0.1);
  border-radius: 20px;
  padding: 16px;
  overflow: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.message-row {
  display: flex;
}

.message-row.user {
  justify-content: flex-end;
}

.bubble {
  max-width: min(72%, 640px);
  padding: 12px 14px;
  border-radius: 16px;
  background: rgba(14, 116, 144, 0.12);
  border: 1px solid rgba(96, 165, 250, 0.15);
}

.message-row.user .bubble {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.25), rgba(34, 197, 94, 0.18));
}

.bubble small {
  display: block;
  margin-bottom: 6px;
  opacity: 0.7;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.bubble p {
  margin: 0;
  line-height: 1.6;
  white-space: pre-wrap;
}

.loading-bubble {
  display: flex;
  align-items: center;
  gap: 12px;
}

.pulse {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #7dd3fc;
  box-shadow: 0 0 18px rgba(125, 211, 252, 0.9);
  animation: pulse 1.2s infinite ease-in-out;
}

@keyframes pulse {
  0%, 100% { transform: scale(0.8); opacity: 0.7; }
  50% { transform: scale(1.25); opacity: 1; }
}

.composer {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  margin-top: 16px;
}

.composer input {
  width: 100%;
  background: rgba(15, 23, 42, 0.82);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 14px;
  padding: 15px 16px;
  color: #e2e8f0;
  outline: none;
}

.composer input:focus {
  border-color: rgba(96, 165, 250, 0.7);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12);
}

.composer button {
  background: linear-gradient(135deg, #60a5fa, #34d399);
  color: #04141d;
  font-weight: 700;
}

.search-panel {
  margin-top: 18px;
  display: grid;
  gap: 10px;
}

.search-card {
  display: block;
  color: #e2e8f0;
  padding: 12px 14px;
  border-radius: 14px;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.12);
  text-decoration: none;
}

.search-card strong {
  display: block;
  margin-bottom: 6px;
}

.search-card span {
  opacity: 0.8;
  line-height: 1.5;
}

@media (max-width: 900px) {
  .jarvis-app {
    display: block;
  }

  .sidebar {
    margin-bottom: 18px;
  }
}

@media (max-width: 560px) {
  .jarvis-app {
    padding: 14px;
  }

  .composer {
    grid-template-columns: 1fr;
  }

  .metrics-grid,
  .config-grid {
    grid-template-columns: 1fr;
  }

  .bubble {
    max-width: 100%;
  }
}
