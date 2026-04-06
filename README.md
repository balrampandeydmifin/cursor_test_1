# React App: Create and Run

This guide explains how to create and run a React app on your machine.

## Prerequisites

- Node.js (LTS recommended)
- npm (comes with Node.js)

Check installed versions:

```bash
node -v
npm -v
```

## 1) Create a React App

Run this command in your terminal:

```bash
npx create-react-app my-react-app
```

This creates a new folder named `my-react-app` with a complete React project setup.

## 2) Go to the Project Folder

```bash
cd my-react-app
```

## 3) Run the App

Start the development server:

```bash
npm start
```

The app will open in your browser at:

`http://localhost:3000`

## Common npm Commands

- `npm start` - Run app in development mode
- `npm test` - Run tests
- `npm run build` - Build app for production
- `npm run eject` - Eject configuration (irreversible)

## Troubleshooting

- If port 3000 is busy, React may suggest another port automatically.
- If dependencies fail to install, delete `node_modules` and `package-lock.json`, then run:

```bash
npm install
```

## Optional: Create App with TypeScript

```bash
npx create-react-app my-react-app --template typescript
```

