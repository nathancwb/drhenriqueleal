// ===================================================
// DR. HENRIQUE LEAL ROSA — 3D Aesthetic Scene (Three.js)
// Real-time WebGL Aesthetic Collagen & Micro-Cannula Geometry
// ===================================================

document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('canvas3d-container');
    if (!container || typeof THREE === 'undefined') return;

    // 1. Scene, Camera & Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 30;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    // 2. Lighting (Medical Luxury Specular Lighting)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
    scene.add(ambientLight);

    const keyLight = new THREE.DirectionalLight(0xC5A880, 2.2); // Warm Gold Key
    keyLight.position.set(20, 20, 20);
    scene.add(keyLight);

    const rimLight = new THREE.DirectionalLight(0x73A5C6, 1.8); // Subtle Cyan/Silver Rim
    rimLight.position.set(-20, -10, -10);
    scene.add(rimLight);

    // 3. 3D Procedural Aesthetic Elements (Micro-Cannula & Collagen Spheres)
    const aestheticGroup = new THREE.Group();

    // A) Sleek Metallic Micro-Cannula (Beveled Cylinder + Tip)
    const cannulaGeo = new THREE.CylinderGeometry(0.2, 0.2, 14, 32);
    const cannulaMat = new THREE.MeshStandardMaterial({
        color: 0xE8DFD0,
        metalness: 0.9,
        roughness: 0.15,
        envMapIntensity: 1.5
    });
    const cannulaMesh = new THREE.Mesh(cannulaGeo, cannulaMat);
    cannulaMesh.position.set(8, -2, 0);
    cannulaMesh.rotation.z = Math.PI / 4.5;
    cannulaMesh.rotation.x = Math.PI / 6;
    aestheticGroup.add(cannulaMesh);

    // Needle Tip
    const tipGeo = new THREE.ConeGeometry(0.2, 1.2, 32);
    const tipMesh = new THREE.Mesh(tipGeo, cannulaMat);
    tipMesh.position.set(0, 7.6, 0);
    cannulaMesh.add(tipMesh);

    // B) Golden Collagen & Hyaluronic Floating Spheres
    const sphereMat = new THREE.MeshStandardMaterial({
        color: 0xC5A880,
        metalness: 0.7,
        roughness: 0.2,
        transparent: true,
        opacity: 0.75
    });

    const spheres = [];
    const sphereGeo = new THREE.SphereGeometry(0.6, 24, 24);

    for (let i = 0; i < 18; i++) {
        const sphere = new THREE.Mesh(sphereGeo, sphereMat);
        const scale = 0.4 + Math.random() * 0.8;
        sphere.scale.set(scale, scale, scale);
        sphere.position.set(
            (Math.random() - 0.5) * 35,
            (Math.random() - 0.5) * 25,
            (Math.random() - 0.5) * 15
        );
        sphere.userData = {
            speedX: (Math.random() - 0.5) * 0.008,
            speedY: (Math.random() - 0.5) * 0.008,
            origY: sphere.position.y
        };
        aestheticGroup.add(sphere);
        spheres.push(sphere);
    }

    // C) Ambient Golden Micro-Particles (Starfield of Rejuvenation)
    const particleCount = 180;
    const particleGeo = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
        positions[i] = (Math.random() - 0.5) * 50;
        positions[i + 1] = (Math.random() - 0.5) * 40;
        positions[i + 2] = (Math.random() - 0.5) * 25;
    }

    particleGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const particleMat = new THREE.PointsMaterial({
        color: 0xDFCAAB,
        size: 0.18,
        transparent: true,
        opacity: 0.6
    });

    const particles = new THREE.Points(particleGeo, particleMat);
    aestheticGroup.add(particles);

    scene.add(aestheticGroup);

    // 4. Cursor Parallax & Scroll Reactive Animation
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;
    let scrollProgress = 0;

    window.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });

    window.addEventListener('scroll', () => {
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
        if (totalHeight > 0) {
            scrollProgress = window.scrollY / totalHeight;
        }
    }, { passive: true });

    // 5. Animation Loop
    function animate() {
        requestAnimationFrame(animate);

        // Smooth cursor follow
        targetX += (mouseX - targetX) * 0.04;
        targetY += (mouseY - targetY) * 0.04;

        // Group gentle rotation + scroll influence
        aestheticGroup.rotation.y = targetX * 0.35 + scrollProgress * Math.PI * 0.8;
        aestheticGroup.rotation.x = -targetY * 0.25;

        // Cannula slow gentle wobble
        cannulaMesh.rotation.y += 0.005;
        cannulaMesh.position.y = -2 + Math.sin(Date.now() * 0.001) * 0.6;

        // Float spheres
        spheres.forEach((s, idx) => {
            s.position.y = s.userData.origY + Math.sin(Date.now() * 0.0015 + idx) * 0.8;
            s.rotation.x += s.userData.speedX;
            s.rotation.y += s.userData.speedY;
        });

        // Slow rotate particles
        particles.rotation.y += 0.0008;

        renderer.render(scene, camera);
    }

    animate();

    // 6. Responsive Resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
});
