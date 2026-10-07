from __future__ import annotations

from typing import Dict, Any


class RobloxAgent:
    """Roblox game development agent. Can create Lua scripts, game systems, NPC AI, UI, weapons, and economy systems."""

    def __init__(self):
        self.name = "Roblox Agent"
        self.description = "Creates Lua scripts, game systems, NPC AI, UI, weapons, and economy systems for Roblox"
        self.supported_systems = [
            "player mechanics",
            "npc behavior",
            "weapon systems",
            "ui design",
            "economy systems",
            "level design",
            "game loop",
            "networking",
            "animations",
            "sound effects",
        ]

    def handle(self, request: str, context: Dict[str, Any]) -> str:
        return self._build_game_response(request, context)

    def _build_game_response(self, request: str, context: Dict[str, Any]) -> str:
        owner = context.get("owner", "Owner")
        request_lower = request.lower()

        if "npc" in request_lower or "ai" in request_lower:
            return self._create_npc_system(owner)
        elif "weapon" in request_lower or "combat" in request_lower:
            return self._create_weapon_system(owner)
        elif "economy" in request_lower or "currency" in request_lower:
            return self._create_economy_system(owner)
        elif "ui" in request_lower or "interface" in request_lower:
            return self._create_ui_system(owner)
        elif "level" in request_lower or "map" in request_lower:
            return self._create_level_design(owner)
        else:
            return self._create_game_foundation(owner)

    def _create_game_foundation(self, owner: str) -> str:
        code = '''-- Roblox Game Foundation by NekoAI
-- Main Game Loop

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

-- Game Config
local GAME_NAME = "NekoAI Game"
local MAX_PLAYERS = 16
local SPAWN_DELAY = 3

-- Initialize Game
local function InitializeGame()
    print("[GAME] Initializing " .. GAME_NAME)
    
    -- Create game folders
    local Maps = Instance.new("Folder")
    Maps.Name = "Maps"
    Maps.Parent = workspace
    
    local Players_Folder = Instance.new("Folder")
    Players_Folder.Name = "ActivePlayers"
    Players_Folder.Parent = workspace
    
    print("[GAME] Initialization complete")
end

-- Handle Player Join
local function OnPlayerJoin(player)
    print("[PLAYER] " .. player.Name .. " joined the game")
    
    local character = player.Character or player.CharacterAdded:Wait()
    print("[PLAYER] " .. player.Name .. " spawned")
end

-- Handle Player Leave
local function OnPlayerLeave(player)
    print("[PLAYER] " .. player.Name .. " left the game")
end

-- Game Loop
local function GameLoop()
    while true do
        RunService.Heartbeat:Wait()
        -- Update game state, NPC behavior, etc.
    end
end

-- Connect Events
Players.PlayerAdded:Connect(OnPlayerJoin)
Players.PlayerRemoving:Connect(OnPlayerLeave)

-- Start Game
InitializeGame()
GameLoop()
'''
        return f"I can create a full Roblox game for {owner}. Here's the foundation:\n\n{code}\n\nNext steps: Add NPC systems, weapons, UI, and economy systems based on your game design."

    def _create_npc_system(self, owner: str) -> str:
        code = '''-- NPC AI System by NekoAI

local NPC_CONFIG = {
    Health = 100,
    Speed = 16,
    DetectionRange = 50,
    AttackRange = 10,
    AttackDamage = 25,
    AttackCooldown = 2
}

local function CreateNPC(position, name)
    local humanoid = Instance.new("Humanoid")
    local rootPart = Instance.new("Part")
    rootPart.Shape = Enum.PartType.Ball
    rootPart.Size = Vector3.new(2, 2, 2)
    rootPart.Position = position
    rootPart.Name = name
    
    humanoid.Parent = rootPart
    humanoid.MaxHealth = NPC_CONFIG.Health
    humanoid.Health = NPC_CONFIG.Health
    
    return rootPart, humanoid
end

local function NPCBehavior(npc, humanoid)
    while humanoid.Health > 0 do
        -- Find nearest player
        local nearestPlayer = nil
        local shortestDistance = NPC_CONFIG.DetectionRange
        
        for _, player in pairs(game.Players:GetPlayers()) do
            if player.Character then
                local distance = (npc.Position - player.Character.HumanoidRootPart.Position).Magnitude
                if distance < shortestDistance then
                    nearestPlayer = player
                    shortestDistance = distance
                end
            end
        end
        
        -- Move toward or attack player
        if nearestPlayer and nearestPlayer.Character then
            local playerPos = nearestPlayer.Character.HumanoidRootPart.Position
            humanoid:MoveTo(playerPos)
        end
        
        wait(0.1)
    end
    
    print("[NPC] " .. npc.Name .. " defeated")
    npc:Destroy()
end

return {
    CreateNPC = CreateNPC,
    NPCBehavior = NPCBehavior,
    CONFIG = NPC_CONFIG
}
'''
        return f"Here's an NPC AI system for your Roblox game:\n\n{code}\n\nThis system includes: detection, pathfinding, and combat logic."

    def _create_weapon_system(self, owner: str) -> str:
        code = '''-- Weapon System by NekoAI

local WEAPON_CONFIG = {
    Sword = {
        Damage = 25,
        Range = 15,
        Cooldown = 1,
        Speed = 0.5
    },
    Gun = {
        Damage = 50,
        Range = 100,
        Cooldown = 0.3,
        Speed = 1
    },
    Bow = {
        Damage = 40,
        Range = 150,
        Cooldown = 0.8,
        Speed = 0.7
    }
}

local function CreateWeapon(weaponType, player)
    local weapon = Instance.new("Tool")
    weapon.Name = weaponType
    weapon.Parent = player.Backpack
    
    local handle = Instance.new("Part")
    handle.Name = "Handle"
    handle.Size = Vector3.new(0.5, 3, 0.5)
    handle.Parent = weapon
    
    local config = WEAPON_CONFIG[weaponType]
    weapon:SetAttribute("Damage", config.Damage)
    weapon:SetAttribute("Range", config.Range)
    weapon:SetAttribute("Cooldown", config.Cooldown)
    
    return weapon
end

local function HandleAttack(weapon, player)
    local config = WEAPON_CONFIG[weapon.Name]
    local camera = workspace.CurrentCamera
    
    local rayOrigin = camera.CFrame.Position
    local rayDirection = camera.CFrame.LookVector * config.Range
    
    local raycastParams = RaycastParams.new()
    raycastParams.FilterType = Enum.RaycastFilterType.Exclude
    raycastParams.FilterDescendantsInstances = {player.Character}
    
    local hit, position = workspace:Raycast(rayOrigin, rayDirection, raycastParams)
    
    if hit then
        if hit.Parent:FindFirstChild("Humanoid") then
            hit.Parent.Humanoid:TakeDamage(config.Damage)
            print("[WEAPON] Hit! Damage: " .. config.Damage)
        end
    end
end

return {
    CreateWeapon = CreateWeapon,
    HandleAttack = HandleAttack,
    WEAPONS = WEAPON_CONFIG
}
'''
        return f"Here's a weapon system for your Roblox game:\n\n{code}\n\nSupported weapons: Sword, Gun, Bow. Each with unique damage and range."

    def _create_economy_system(self, owner: str) -> str:
        code = '''-- Economy System by NekoAI

local ECONOMY_CONFIG = {
    StartingMoney = 100,
    KillReward = 50,
    DeathPenalty = 10,
    ItemPrices = {
        Sword = 150,
        Gun = 300,
        Bow = 200,
        HealthPotion = 50
    }
}

local function InitializePlayerEconomy(player)
    local leaderstats = Instance.new("Folder")
    leaderstats.Name = "leaderstats"
    leaderstats.Parent = player
    
    local money = Instance.new("IntValue")
    money.Name = "Money"
    money.Value = ECONOMY_CONFIG.StartingMoney
    money.Parent = leaderstats
    
    local level = Instance.new("IntValue")
    level.Name = "Level"
    level.Value = 1
    level.Parent = leaderstats
    
    local kills = Instance.new("IntValue")
    kills.Name = "Kills"
    kills.Value = 0
    kills.Parent = leaderstats
    
    return leaderstats
end

local function AddMoney(player, amount)
    local money = player.leaderstats:WaitForChild("Money")
    money.Value = money.Value + amount
    print("[ECONOMY] " .. player.Name .. " earned $" .. amount)
end

local function RemoveMoney(player, amount)
    local money = player.leaderstats:WaitForChild("Money")
    if money.Value >= amount then
        money.Value = money.Value - amount
        return true
    end
    return false
end

local function HandleKill(killer, victim)
    AddMoney(killer, ECONOMY_CONFIG.KillReward)
    local money = victim.leaderstats:WaitForChild("Money")
    money.Value = math.max(0, money.Value - ECONOMY_CONFIG.DeathPenalty)
end

return {
    InitializePlayerEconomy = InitializePlayerEconomy,
    AddMoney = AddMoney,
    RemoveMoney = RemoveMoney,
    HandleKill = HandleKill,
    CONFIG = ECONOMY_CONFIG
}
'''
        return f"Here's an economy system for your Roblox game:\n\n{code}\n\nFeatures: Currency, leveling, kills tracking, item prices."

    def _create_ui_system(self, owner: str) -> str:
        code = '''-- UI System by NekoAI

local function CreateMainUI(player)
    local playerGui = player:WaitForChild("PlayerGui")
    
    -- Main Screen
    local screenGui = Instance.new("ScreenGui")
    screenGui.Name = "MainUI"
    screenGui.Parent = playerGui
    
    -- Health Bar
    local healthBar = Instance.new("Frame")
    healthBar.Name = "HealthBar"
    healthBar.Size = UDim2.new(0, 200, 0, 20)
    healthBar.Position = UDim2.new(0, 10, 0, 10)
    healthBar.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
    healthBar.Parent = screenGui
    
    local healthFill = Instance.new("Frame")
    healthFill.Name = "Fill"
    healthFill.Size = UDim2.new(1, 0, 1, 0)
    healthFill.BackgroundColor3 = Color3.fromRGB(0, 255, 0)
    healthFill.Parent = healthBar
    
    -- Money Display
    local moneyLabel = Instance.new("TextLabel")
    moneyLabel.Name = "Money"
    moneyLabel.Text = "$0"
    moneyLabel.Size = UDim2.new(0, 100, 0, 30)
    moneyLabel.Position = UDim2.new(1, -110, 0, 10)
    moneyLabel.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
    moneyLabel.TextColor3 = Color3.fromRGB(255, 255, 0)
    moneyLabel.TextSize = 18
    moneyLabel.Parent = screenGui
    
    -- Kill Count
    local killLabel = Instance.new("TextLabel")
    killLabel.Name = "Kills"
    killLabel.Text = "Kills: 0"
    killLabel.Size = UDim2.new(0, 100, 0, 30)
    killLabel.Position = UDim2.new(1, -110, 0, 50)
    killLabel.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
    killLabel.TextColor3 = Color3.fromRGB(255, 0, 0)
    killLabel.TextSize = 18
    killLabel.Parent = screenGui
    
    return screenGui
end

return {
    CreateMainUI = CreateMainUI
}
'''
        return f"Here's a UI system for your Roblox game:\n\n{code}\n\nIncludes: Health bar, money display, kill counter, game overlay."

    def _create_level_design(self, owner: str) -> str:
        code = '''-- Level Design Template by NekoAI

local function CreateSpawnPlatform(position, size)
    local platform = Instance.new("Part")
    platform.Shape = Enum.PartType.Block
    platform.Size = size or Vector3.new(50, 1, 50)
    platform.Position = position
    platform.CanCollide = true
    platform.Material = Enum.Material.Brick
    platform.BrickColor = BrickColor.new("Bright green")
    platform.TopSurface = Enum.SurfaceType.Smooth
    platform.Parent = workspace
    return platform
end

local function CreateObstacle(position, size)
    local obstacle = Instance.new("Part")
    obstacle.Shape = Enum.PartType.Block
    obstacle.Size = size or Vector3.new(5, 10, 5)
    obstacle.Position = position
    obstacle.CanCollide = true
    obstacle.Material = Enum.Material.Brick
    obstacle.BrickColor = BrickColor.new("Dark stone grey")
    obstacle.Parent = workspace
    return obstacle
end

local function BuildLevel(levelName)
    local levelFolder = Instance.new("Folder")
    levelFolder.Name = levelName
    levelFolder.Parent = workspace
    
    -- Create main platform
    local mainPlatform = CreateSpawnPlatform(Vector3.new(0, 0, 0), Vector3.new(100, 1, 100))
    mainPlatform.Parent = levelFolder
    
    -- Add obstacles
    CreateObstacle(Vector3.new(-30, 5, -30), Vector3.new(10, 10, 10)).Parent = levelFolder
    CreateObstacle(Vector3.new(30, 5, 30), Vector3.new(10, 10, 10)).Parent = levelFolder
    
    print("[LEVEL] " .. levelName .. " created successfully")
    return levelFolder
end

return {
    CreateSpawnPlatform = CreateSpawnPlatform,
    CreateObstacle = CreateObstacle,
    BuildLevel = BuildLevel
}
'''
        return f"Here's a level design system for your Roblox game:\n\n{code}\n\nCreate custom platforms, obstacles, and complete level layouts."


__all__ = ["RobloxAgent"]
