# Testing Guide for React Money Manager Project

## Purpose

This document describes the test approach for the React Money Manager app. It covers test types, tooling, and recommended workflows.

## Testing Goals

- Ensure core features work correctly
- Protect against regressions
- Validate UX and user flows
- Support reliable deployments

## Test Types

### 1. Unit Tests

- Test individual functions, components, and utilities
- Keep tests fast and isolated
- Example tools: Jest, React Testing Library

### 2. Integration Tests

- Test component combinations and state interactions
- Validate how features work together
- Example tools: React Testing Library

### 3. End-to-End (E2E) Tests

- Test full user flows in a browser-like environment
- Cover scenarios such as sign-in, transaction creation, and budget review
- Example tools: Cypress, Playwright

### 4. Visual / UI Tests (Optional)

- Check UI appearance and layout changes
- Example tools: Storybook with snapshot tests, Percy

## Recommended Tooling

- `Jest` for unit and integration tests
- `React Testing Library` for React component tests
- `Cypress` for end-to-end testing
- `ESLint` and `Prettier` for code quality and consistency

## Test Structure

Suggested folder layout:

- `src/components/` - component test files alongside components
- `src/pages/` - page-level tests
- `src/utils/` - utility tests
- `cypress/` - E2E tests

## Example Test Scenarios

### Unit Test Scenarios

- Transaction form validation
- Category filter logic
- Summary calculation functions
- Local storage save/load functions

### Integration Test Scenarios

- Add transaction and update dashboard totals
- Edit transaction and refresh list
- Apply filters and verify filtered results
- Theme toggle persistence

### E2E Test Scenarios

- User adds a new income transaction
- User adds a new expense transaction
- User deletes a transaction
- User navigates between dashboard and reports
- User switches between light/dark mode

## Running Tests

### Run all unit and integration tests

```bash
npm test
```

### Run end-to-end tests

```bash
npx cypress open
```

or headless:

```bash
npx cypress run
```

## Testing Workflow

1. Write tests before or alongside new features.
2. Run targeted tests after implementing changes.
3. Add regression tests for any bug fixes.
4. Review test coverage and update tests for major UI changes.

## Quality Metrics

- Test coverage for core financial flows
- Stable CI test runs on each pull request
- Minimal flaky tests
- Clear test names and assertions

## Notes

- Keep tests deterministic and independent
- Mock external APIs or data stores when possible
- Use data attributes or accessible roles for selectors in UI tests
