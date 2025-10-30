const rackWall = document.getElementById('rack-wall');
const versionLabel = document.getElementById('version');

if (window.blinkyLights) {
  versionLabel.textContent = `Version ${window.blinkyLights.version} · Electron ${window.blinkyLights.electron}`;
}

const rackCount = 6;
const unitsPerRack = 12;
const lightsPerUnit = 8;
const channelPool = ['ok', 'ok', 'warn', 'ok', 'err', 'ok', 'warn'];

const lights = [];

const createLight = () => {
  const light = document.createElement('span');
  light.className = 'light';
  light.dataset.channel = channelPool[Math.floor(Math.random() * channelPool.length)];
  light.dataset.intensity = (60 + Math.random() * 30).toFixed(0);
  return light;
};

const createUnit = (index) => {
  const unit = document.createElement('article');
  unit.className = 'rack-unit';

  const header = document.createElement('header');
  header.className = 'rack-unit__label';
  header.textContent = `U${String(unitsPerRack - index).padStart(2, '0')}`;
  unit.appendChild(header);

  const tray = document.createElement('div');
  tray.className = 'light-tray';

  for (let i = 0; i < lightsPerUnit; i += 1) {
    const light = createLight();
    tray.appendChild(light);
    lights.push(light);
  }

  unit.appendChild(tray);

  const meter = document.createElement('div');
  meter.className = 'load-meter';

  const fill = document.createElement('div');
  fill.className = 'load-meter__fill';
  fill.style.width = `${30 + Math.random() * 60}%`;
  meter.appendChild(fill);

  unit.appendChild(meter);

  return unit;
};

const createRack = (rackIndex) => {
  const rack = document.createElement('section');
  rack.className = 'rack';
  rack.dataset.rack = rackIndex + 1;

  const banner = document.createElement('div');
  banner.className = 'rack__banner';
  banner.textContent = `RACK ${rackIndex + 1}`;
  rack.appendChild(banner);

  for (let unitIndex = 0; unitIndex < unitsPerRack; unitIndex += 1) {
    rack.appendChild(createUnit(unitIndex));
  }

  rackWall.appendChild(rack);
};

for (let rackIndex = 0; rackIndex < rackCount; rackIndex += 1) {
  createRack(rackIndex);
}

const animateLight = (light) => {
  const toggle = () => {
    const active = Math.random() > 0.4;
    light.classList.toggle('is-on', active);
    const intensity = active ? light.dataset.intensity : 20 + Math.random() * 10;
    light.style.setProperty('--intensity', intensity);
    const delay = active
      ? 80 + Math.random() * 250
      : 200 + Math.random() * 900;
    setTimeout(toggle, delay);
  };

  toggle();
};

lights.forEach((light) => animateLight(light));

const createSweep = () => {
  const sweep = document.createElement('div');
  sweep.className = 'activity-sweep';
  rackWall.appendChild(sweep);

  const run = () => {
    sweep.classList.remove('is-active');
    // Force reflow so the animation restarts cleanly.
    void sweep.offsetWidth;
    sweep.classList.add('is-active');
    setTimeout(run, 3000 + Math.random() * 4000);
  };

  run();
};

createSweep();
