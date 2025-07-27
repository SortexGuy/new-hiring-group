from __future__ import annotations

from pathlib import Path
import typing as t

import rio
import httpx
import asyncio
from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime

from . import components as comps

SERVER_URL = 'http://localhost:8080/'

# Define a theme for Rio to use.
#
# You can modify the colors here to adapt the appearance of your app or website.
# The most important parameters are listed, but more are available! You can find
# them all in the docs
#
# https://rio.dev/docs/api/theme
theme = rio.Theme.from_colors(
    primary_color=rio.Color.from_hex('01dffdff'),
    secondary_color=rio.Color.from_hex('0083ffff'),
    mode='dark',
)


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    completed: bool
    created_at: str


class TaskManager(rio.Component):
    tasks: List[Task] = []
    new_task_title: str = ''
    new_task_description: str = ''
    new_task_priority: str = 'medium'
    loading: bool = False
    stats: Dict[str, int] = {}

    async def on_mount(self) -> None:
        await self.load_tasks()
        await self.load_stats()

    async def load_tasks(self) -> None:
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get('http://localhost:8000/api/tasks/')
                if response.status_code == 200:
                    data = response.json()
                    self.tasks = [Task(**task) for task in data]
        except Exception as e:
            print(f'Error loading tasks: {e}')
        finally:
            self.loading = False

    async def load_stats(self) -> None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    'http://localhost:8000/api/tasks/stats/'
                )
                if response.status_code == 200:
                    self.stats = response.json()
        except Exception as e:
            print(f'Error loading stats: {e}')

    async def add_task(self) -> None:
        if not self.new_task_title.strip():
            return

        try:
            async with httpx.AsyncClient() as client:
                task_data = {
                    'title': self.new_task_title,
                    'description': self.new_task_description,
                    'priority': self.new_task_priority,
                    'completed': False,
                }
                response = await client.post(
                    'http://localhost:8000/api/tasks/', json=task_data
                )
                if response.status_code == 201:
                    self.new_task_title = ''
                    self.new_task_description = ''
                    self.new_task_priority = 'medium'
                    await self.load_tasks()
                    await self.load_stats()
        except Exception as e:
            print(f'Error adding task: {e}')

    async def toggle_task(self, task_id: int) -> None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f'http://localhost:8000/api/tasks/{task_id}/toggle_complete/'
                )
                if response.status_code == 200:
                    await self.load_tasks()
                    await self.load_stats()
        except Exception as e:
            print(f'Error toggling task: {e}')

    async def delete_task(self, task_id: int) -> None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(
                    f'http://localhost:8000/api/tasks/{task_id}/'
                )
                if response.status_code == 204:
                    await self.load_tasks()
                    await self.load_stats()
        except Exception as e:
            print(f'Error deleting task: {e}')

    def get_priority_color(self, priority: str) -> rio.Color:
        colors = {
            'low': rio.Color.GREEN,
            'medium': rio.Color.ORANGE,
            'high': rio.Color.RED,
        }
        return colors.get(priority, rio.Color.GREY)

    def build(self) -> rio.Component:
        return rio.Column(
            # Header
            rio.Row(
                rio.Text(
                    'Task Manager',
                    style=rio.TextStyle(font_size=2.5, font_weight='bold'),
                ),
                rio.Spacer(),
                rio.Button(
                    'Refresh',
                    on_press=self.load_tasks,
                ),
                spacing=1,
                margin=1,
            ),
            spacing=1,
        )


# Create Rio App
app = rio.App(
    name='Talentos Asociados',
    theme=theme,
    assets_dir=Path(__file__).parent / 'assets',
)
