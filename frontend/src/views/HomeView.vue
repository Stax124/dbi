<template>
  <NCard title="Trending" class="main-card">
    <NGrid cols="3" x-gap="12">
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
    </NGrid>
  </NCard>

  <NCard title="Newest" class="main-card">
    <NGrid cols="3" x-gap="12">
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
      <NGi>
        <NSkeleton height="168px" />
      </NGi>
    </NGrid>
  </NCard>

  <NCard title="Feed" class="main-card">
    <NGrid cols="4" x-gap="12">
      <NGi span="3" style="display: flex; flex-direction: column; gap: 12px 0">
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
        <NCard
          :content-style="{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            gap: '0 24px',
            height: '168px'
          }"
          style="height: 168px"
        >
          <!-- <NSkeleton /> -->
          <img
            src="https://uploads.golmedia.net/uploads/articles/article_media/14748410301702468268gol1.jpg"
            style="width: auto; height: 100%"
          />
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam voluptatum, quibusdam,
            voluptate, quia quod voluptas quos voluptatibus quae doloribus quidem fugiat. Quisquam
            voluptatum, quibusdam, voluptate, quia quod voluptas quos voluptatibus quae doloribus
            quidem fugiat.
          </p>
        </NCard>
      </NGi>
      <NGi>Other Stuff</NGi>
    </NGrid>
  </NCard>
</template>

<script setup lang="ts">
import { NCard, NGi, NGrid, NSkeleton } from 'naive-ui'
</script>

<style scoped>
.main-card:not(:last-child) {
  margin-bottom: 16px;
}
</style>
