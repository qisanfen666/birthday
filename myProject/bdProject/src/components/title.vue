<script setup lang="ts">
import { ref } from 'vue';

const showMeteor = ref(false); // 控制流星的显示

function startMeteor() {
  showMeteor.value = true;
  setTimeout(() => {
    showMeteor.value = false; // 流星效果持续一段时间后消失
  }, 25000); // 流星持续 25 秒
}
defineExpose({
  startMeteor, // 暴露给父组件调用
});
</script>

<template>
  <div v-if="showMeteor" class="meteor">
    <span class="meteor-trail"></span>
    <span class="meteor-text">Happy Birthday</span>
  </div>
</template>

<style>
/* 流星容器 */
.meteor {
  position: fixed;
  top: -290px;
  right: -900px; /* 初始位置在屏幕右侧外 */
  display: flex;
  align-items: center;
  animation: meteorMove 20s linear forwards; /* 流星从右到左移动 */
  z-index: 20;
}

/* 流星拖尾 */
.meteor-trail {
  width: 150px;
  height: 20px;
  background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.8));
  border-radius: 5px;
  margin-right: 10px;
}

/* 流星文字 */
.meteor-text {
  font-size: 72px;
  font-weight: bold;
  color: #ff69b4;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  white-space: nowrap;
}

/* 流星动画 */
@keyframes meteorMove {
  0% {
    right: -900px; /* 从屏幕右侧外开始 */
    opacity: 0;
  }
  10% {
    opacity: 1;
  }
  100% {
    right: 100%; /* 移动到屏幕左侧外 */
    opacity: 0;
  }
}
</style>