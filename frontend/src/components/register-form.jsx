'use client'

import { zodResolver } from '@hookform/resolvers/zod'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { Button } from '@/components/ui/button'
import {
	Form,
	FormControl,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from '@/components/ui/select'

const formSchema = z.object({
	name: z.string().min(3, { message: 'Name must be at least 3 characters' }),
	email: z.string().email({ message: 'Invalid email' }),
	password: z
		.string()
		.min(8, { message: 'Password must be at least 8 characters' }),
	confirmPassword: z.string(),
	accountType: z.enum(['student', 'teacher']),
})

export default function RegisterForm() {
	const form = useForm({
		defaultValues: {
			name: '',
			email: '',
			password: '',
			confirmPassword: '',
			accountType: '',
		},
	})

	function onSubmit(values) {
		console.log(values)
	}

	return (
		<Form {...form}>
			<form onSubmit={form.handleSubmit(onSubmit)} className='space-y-2'>
				<FormField
					control={form.control}
					name='name'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Name</FormLabel>
							<FormControl>
								<Input placeholder='John Doe' {...field} />
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='email'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Email</FormLabel>
							<FormControl>
								<Input type='email' placeholder='john@dev.com' {...field} />
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='password'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Password</FormLabel>
							<FormControl>
								<Input type='password' {...field} />
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='confirmPassword'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Confirm Password</FormLabel>
							<FormControl>
								<Input type='password' {...field} />
							</FormControl>
							<FormMessage />
						</FormItem>
					)}
				/>
				<FormField
					control={form.control}
					name='accountType'
					render={({ field }) => (
						<FormItem>
							<FormLabel>Account Type</FormLabel>
							<Select onValueChange={field.onChange} defaultValue={field.value}>
								<FormControl>
									<SelectTrigger>
										<SelectValue placeholder='Select an account type' />
									</SelectTrigger>
								</FormControl>
								<SelectContent>
									<SelectItem value='student'>Student</SelectItem>
									<SelectItem value='teacher'>Teacher</SelectItem>
								</SelectContent>
							</Select>
							<FormMessage />
						</FormItem>
					)}
				/>
				<Button type='submit' className='w-full'>
					Submit
				</Button>
			</form>
		</Form>
	)
}

// ;<form>
// 	<div className='grid w-full items-center gap-4'>
// 		<div className='flex flex-col space-y-1.5'>
// 			<Label htmlFor='name'>Name</Label>
// 			<Input id='name' placeholder='Name of your project' />
// 		</div>
// 		<div className='flex flex-col space-y-1.5'>
// 			<Label htmlFor='framework'>Framework</Label>
// 			<Select>
// 				<SelectTrigger id='framework'>
// 					<SelectValue placeholder='Select' />
// 				</SelectTrigger>
// 				<SelectContent position='popper'>
// 					<SelectItem value='next'>Next.js</SelectItem>
// 					<SelectItem value='sveltekit'>SvelteKit</SelectItem>
// 					<SelectItem value='astro'>Astro</SelectItem>
// 					<SelectItem value='nuxt'>Nuxt.js</SelectItem>
// 				</SelectContent>
// 			</Select>
// 		</div>
// 	</div>
// </form>
