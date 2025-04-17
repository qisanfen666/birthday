<script setup lang="ts">
import { onMounted } from 'vue';
import Letter from './components/letter.vue';

onMounted(() => {
  createConfetti();
});

function createConfetti() {
  const container = document.querySelector('.background-container');
  if (!container) return;

  for (let i = 0; i < 20; i++) {
    const confetti = document.createElement('div');
    confetti.className = 'confetti';
    confetti.style.left = Math.random() * 100 + 'vw';
    confetti.style.animationDelay = Math.random() * 5 + 's';
    confetti.style.backgroundColor = getRandomColor();
    container.appendChild(confetti);
  }
}

function getRandomColor() {
  const colors = ['#FF5733', '#33FF57', '#3357FF', '#FFD700', '#FF33A1'];
  return colors[Math.floor(Math.random() * colors.length)];
}
</script>

<template>
  <div class="background-container">
    <Letter></Letter>
  </div>
</template>

<style>
.background-container {
  width: 98%;
  height: 95vh; /* 设置全屏高度 */
  background-image: url('./assets/party.jpg'); /* 替换为你的图片路径 */
  background-size: cover; /* 确保图片覆盖整个容器 */
  background-position: center; /* 居中显示图片 */
  background-repeat: no-repeat; /* 防止图片重复 */
  border: 10px solid #ffd700;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  border-radius: 15px;
  position: relative; /* 确保子元素定位相对于容器 */
  overflow: hidden; /* 防止内容溢出 */
}
.confetti {
  position: absolute;
  top: -10px;
  width: 10px;
  height: 30px;
  opacity: 0.8;
  animation: fall 5s linear infinite;
}

@keyframes fall {
  0% {
    transform: translateY(0) rotate(0deg);
  }
  100% {
    transform: translateY(95vh) rotate(360deg);
  }
}
</style>
