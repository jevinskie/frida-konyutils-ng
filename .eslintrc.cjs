module.exports = {
    extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
    parser: "@typescript-eslint/parser",
    plugins: ["@typescript-eslint"],
    env: { node: true, commonjs: true, es2020: true },
    overrides: [
        {
            files: [".eslintrc.js", "frida_konyutils_ng/agent/*.ts"],
            parserOptions: {
                sourceType: "script",
                ecmaFeatures: {
                    impliedStrict: true,
                },
            },
            rules: {
                quotes: ["error", "double"],
                semi: ["error", "always"],
            },
        },
    ],
};
