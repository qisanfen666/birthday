<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Title from './title.vue'; // 引入触发流星的函数

const showEnvelope = ref(false);
const isEnvelopeOpen = ref(true); // 信封是否打开
const showSeal = ref(true);
const showLetter = ref(false); // 是否显示信纸

const titleRef = ref<{ startMeteor: () => void } | null>(null);

async function toggleEnvelope() {
    if (showSeal.value) {
    // 点击时让封口章掉落
    showSeal.value = false;
    isEnvelopeOpen.value = false; 
    // 章掉落后再打开信封
    await setTimeout(() => {
        showLetter.value = true; // 延迟显示信纸
    }, 500);
    await setTimeout(() => {
       if(titleRef.value){
        titleRef.value.startMeteor(); // 调用流星函数
       }
    }, 1000);
      
  } else {
    isEnvelopeOpen.value = !isEnvelopeOpen.value; // 切换信封状态
  }
}

onMounted(() => {
  // 延迟显示信封
  setTimeout(() => {
    showEnvelope.value = true;
  }, 1000); // 1秒后显示信封
});
</script>

<template>
    <div class="envelope-container" @click="toggleEnvelope">
    <!-- 信封 -->
    <div v-if="showEnvelope" class="envelope" :class="{ open: isEnvelopeOpen }">
      <div class="envelope-flap">
        <!-- 封口章 -->
        <div v-if="showSeal" class="seal"></div>
      </div>
      <div class="envelope-body">
        <!-- 信封内部内容 -->
        <div class="letter-content"></div>
      </div>
    </div>
     <!-- 信纸 -->
     <div v-if="showLetter" class="letter">
      <div class="letter-content">
        <h1>惊喜！</h1>
        <p>这是信纸上的文字内容。</p>
        <img src="./assets/sample-image.png" alt="图案" />
      </div>
    </div>
    <!-- 流星组件 -->
    <Title ref="titleRef"></Title>
  </div>
</template>

<style>
.envelope-container {
  position: absolute;
  top: 50%;
  left: 45%;
  transform: translate(-50%, -50%); /* 信封居中 */
  z-index: 10; /* 确保信封在背景图片之上 */
  cursor:pointer;
}

/* 信封容器 */
.envelope {
  position: absolute;
  bottom: -200px; /* 初始位置在屏幕外 */
  width: 150px;
  height: 100px;
  animation: slideUp 2s ease-out forwards; /* 弹出动画 */
  transition: transform 0.5s ease;
}

/* 信封主体 */
.envelope-body {
  width: 100%;
  height: 85%;
  background: #4ab6f5;
  border: 2px solid #a88888;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  position: relative;
  z-index: 1;
}

/* 信封盖 */
.envelope-flap {
  width: 100%;
  height: 50%;
  background: #5367eb;
  border: 1px solid #ccc;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  position: absolute;
  top: -51%;
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  z-index: 2;
  transition: transform 0.5s ease; /* 添加平滑过渡效果 */
  transform-origin: bottom; /* 设置翻转的中心点 */
}

/* 信封打开时的样式 */
.envelope.open .envelope-flap {
  transform: rotateX(-180deg); /* 翻转信封盖 */
  
  transition: transform 1s ease;
}

.seal {
  width: 40px;
  height: 40px;
  background: rgb(170, 87, 218);
  border-radius: 50%;
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translate(-50%, 0);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  z-index: 3;
  transition: top 0.5s ease; /* 添加掉落动画 */
}

.seal.hidden {
  top: 120%; /* 掉落到信封外 */
  opacity: 0.2; /* 渐隐 */
  
}
/* 信纸 */
.letter {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0); /* 初始状态：缩小 */
  width: 450px;
  height: 300px;
  background: #f4f7d5;
  border: 2px solid #ccc;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  z-index: 5;
  animation: flyOut 1s ease-out forwards, grow 1s ease-out 1s forwards;
}

/* 信纸内容 */
.letter-content {
  padding: 20px;
  text-align: center;
}

.letter-content h1 {
  font-size: 24px;
  color: #333;
}

.letter-content p {
  font-size: 16px;
  color: #666;
}

.letter-content img {
  width: 100px;
  height: auto;
  margin-top: 10px;
}

/* 信纸飞出动画 */
@keyframes flyOut {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
  100% {
    transform: translate(-30%, -150px) scale(1);
    opacity: 1;
  }
}

/* 信纸变大动画 */
@keyframes grow {
  0% {
    transform: translate(-30%, -150px) scale(1);
  }
  100% {
    transform: translate(-30%, -150px) scale(1.2);
  }
}

/* 弹出动画 */
@keyframes slideUp {
  0% {
    bottom: -200px;
    opacity: 0;
  }
  100% {
    bottom: 20px;
    opacity: 1;
  }
}
</style>